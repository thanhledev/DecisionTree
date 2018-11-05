import decimal


class CandidateAttribute:

    # Initializer / Instance Attributes
    def __init__(self, name: str, gain: float, values: []):
        self.name = name
        self.gain = decimal.Decimal(gain)
        self.values = values

    # instance method
    def description(self):
        return "Attribute {} has information gain {} and values {}".format(self.name, self.gain, self.values)

    # comparable methods
    def __eq__(self, other):
        return self.gain == other.gain and self.name != other.name

    def __lt__(self, other):
        if self.gain < other.gain:
            return True
        elif self.gain == other.gain:
            if len(self.name) > len(other.name):
                return False
            elif len(self.name) == len(other.name):
                return min(self.name, other.name)
            else:
                return True
        else:
            return False
