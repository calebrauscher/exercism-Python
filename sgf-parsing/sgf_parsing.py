import re


class SgfTree(object):
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(input_string):
    if re.search(r"(^$)|(\(\))|(^;$)", input_string):
        raise ValueError("Empty String")
    if re.search(r"(\(;\))", input_string):
        return SgfTree()
    if re.search(r"\(;[A-Z]\)", input_string):
        raise ValueError("Property with no delimiter")
    if re.search(r"\(;([A-Z][a-z]|[a-z])\[\w\]\)", input_string):
        raise ValueError("Lowercase property")
    nodes = re.findall(r";([A-Z]+)\[([A-Z]+)\]]", input_string)
    print(nodes)


if __name__ == "__main__":
    input_string = "(;A[B];B[C])"
    parse(input_string)