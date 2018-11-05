class TreeAttribute:

    # Initializer / Instance Attributes
    def __init__(self, attribute_name=None, attribute_values=None):
        if attribute_name is not None:
            self.attribute_name = attribute_name
        else:
            self.attribute_name = ""
        if attribute_values is not None:
            self.attribute_values = attribute_values
        else:
            self.attribute_values = []

    # instance method
    def description(self):
        if self.attribute_name is not None and self.attribute_values is not None:
            print("All values of %s are:\n" % self.attribute_name)
            for av in self.attribute_values:
                print(av.description())
            print("\n")

    def update_attribute_list(self, new_attr):
        if not any(attr.value == new_attr.value for attr in self.attribute_values):
            self.attribute_values.append(new_attr)
