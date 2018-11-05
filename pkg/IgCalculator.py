import pandas as pd
import numpy as np

def entropy(dataframe: pd.DataFrame, attribute_name: str) -> float:
    # initialize entropy value
    entropy_val = 0.0

    # get total row in dataframe [0] for rows, [1] for columns
    total = dataframe.shape[0]

    # get all unique values of the attribute
    attribute_values = dataframe[attribute_name].unique().tolist()

    for val in attribute_values:
        # get and count all rows of attribute_name that have the same value
        attr_occur = len(dataframe.index[dataframe[attribute_name] == val].tolist())

        entropy_val += (-attr_occur/total)*(np.log2(attr_occur/total))

    return entropy_val


def information_gain(dataframe: pd.DataFrame, concept_attribute_name: str, classifier_attribute_name: str) -> float:
    # first, calculate the entropy origin of the target concept
    target_concept_entropy = entropy(dataframe, concept_attribute_name)

    # next, initialize the classifier attribute entropy and information gain values
    classifier_attribute_entropy = 0.0

    # next, get total row in dataframe
    total = dataframe.shape[0]

    # next, get all unique values of the classifier attribute
    classifier_attribute_values = dataframe[classifier_attribute_name].unique().tolist()

    for val in classifier_attribute_values:
        # get all row indexes of the particular value
        row_indexes = dataframe.index[dataframe[classifier_attribute_name] == val].tolist()

        # clone and cut current dataframe to a new dataframe
        classifier_attribute_value_df = dataframe.iloc[row_indexes]

        # calculate classifier attribute entropy
        classifier_attribute_entropy += (len(row_indexes)/total)*entropy(classifier_attribute_value_df, concept_attribute_name)

    # calculate the information gain of the current classifier attribute
    classifier_information_gain = target_concept_entropy - classifier_attribute_entropy

    return classifier_information_gain
