class AttributeValue:

    # Initializer / Instance Attributes
    def __init__(self, value=None, row_indexes=None):
        if value is not None:
            self.value = value
        else:
            self.value = ""
        if row_indexes is not None:
            self.row_indexes = row_indexes
        else:
            self.row_indexes = []

    # instance method
    def description(self):
        return "{} is appeared in {}".format(self.value, self.row_indexes)
