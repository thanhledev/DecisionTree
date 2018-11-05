import pandas as pd
from pkg.CandidateAttribute import CandidateAttribute
from pkg.DNode import DecisionTreeNode
from pkg.IgCalculator import *
import decimal
from graphviz import Source

def decision_tree_id3(filename: str, concept_attribute_name: str):

    # process the csv file, load to pandas dataframe
    dataframe = pd.read_csv(filename, na_values=["."])

    # get all attribute columns except the target concept column name
    attribute_names = [name for name in dataframe.columns.tolist() if name != concept_attribute_name]

    # initialize the tree nodes array
    tree_nodes = []

    # begin algorithm
    build_decision_tree_id3(tree_nodes, dataframe, concept_attribute_name, attribute_names, None, None)

    # initialize the node description
    node_des = node_links = ""
    # print the tree
    for node in tree_nodes:
        node_des += node.describe_node()
        node_links += node.describe_link()

    print(repr(node_des + node_links))

    # tree graph
    src = Source('digraph Tree {' + node_des + node_links + '}')
    src.render('decision_tree.gv', view=True)
    input("Press enter to continue")


def build_decision_tree_node(length: int, label: str, ig_value: float, is_leaf: bool, parent_idx: int,
                             parent_branch: str) -> DecisionTreeNode:
    node_index = length if length > 0 else 0
    node_label = label
    node_ig = decimal.Decimal(ig_value)
    node_parent_idx = parent_idx if parent_idx is not None else None
    node_parent_branch = parent_branch if parent_branch is not None else None

    return DecisionTreeNode(node_index, node_label, node_ig, is_leaf, node_parent_idx, node_parent_branch)


def build_decision_tree_id3(nodes: [], dataframe: pd.DataFrame, concept_attribute_name: str, attributes: [],
                            parent_idx: int, parent_branch: str):

    # process the dataframe by concept_attribute_name
    concept_attribute_values = dataframe[concept_attribute_name].unique().tolist()

    if len(concept_attribute_values) == 1:
        # if single value, create a leaf node and append
        nodes.append(build_decision_tree_node(len(nodes), concept_attribute_values[0],
                                  0.0, True, parent_idx, parent_branch))
    else:
        # initialize the candidate attributes array
        candidate_attrs = []

        # begin process the attributes
        for attr in attributes:
            # get all unique values of the attr
            attr_values = dataframe[attr].unique().tolist()

            # calculate the information gain of attr
            attr_ig = decimal.Decimal(information_gain(dataframe, concept_attribute_name, attr))

            candidate_attrs.append(CandidateAttribute(attr, attr_ig, attr_values))

        # sort the candidate attributes array
        candidate_attrs.sort(reverse=True)

        # get the attr which has the highest information gain
        highest_candidate = candidate_attrs[0]

        # create a new node
        decision_node = build_decision_tree_node(len(nodes), highest_candidate.name,
                                 highest_candidate.gain, False, parent_idx, parent_branch)

        # append node to nodes
        nodes.append(decision_node)

        # recursive
        for val in highest_candidate.values:
            # strip current dataframe
            new_dataframe = dataframe.iloc[dataframe.index[dataframe[highest_candidate.name] == val].tolist()].reset_index(drop=True)

            # strip attributes list
            new_attributes = [attr for attr in attributes if attr != highest_candidate.name]

            # recall
            build_decision_tree_id3(nodes, new_dataframe, concept_attribute_name, new_attributes, decision_node.index,
                                    val)
