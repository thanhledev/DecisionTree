import decimal


class DecisionTreeNode:

    # Initializer / Instance Attributes
    def __init__(self, index: int, label: str, information_gain: float,
                 is_leaf: bool, parent_idx: int, parent_branch: str):
        self.index = index
        self.label = label
        self.information_gain = decimal.Decimal(information_gain)
        self.is_leaf = is_leaf
        self.parent_idx = parent_idx
        self.parent_branch = parent_branch

    # instance method
    def describe_node(self) -> str:
        node_label_value = self.label

        if not self.is_leaf:
            node_label_value += "\n IG:%.4f" % float(self.information_gain)

        return "{} [label=\"{}\" shape={shape}];".format(self.index, node_label_value, shape="box" if
                                                                 self.is_leaf is True else "ellipse")

    def describe_link(self) -> str:
        if self.parent_idx is not None and self.parent_branch is not None:
            return "{} -> {} [labeldistance=2.5, labelangle=45, headlabel=\"{}\"];".format(self.parent_idx,
                                          self.index, self.parent_branch)
        return ""
