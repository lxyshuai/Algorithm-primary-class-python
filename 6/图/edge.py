class Edge(object):
    def __init__(self, weight, from_node, to_node):
        self.weight = weight
        self.from_node = from_node
        self.to_node = to_node

    def __cmp__(self, other):
        if self.weight > other.weight:
            return 1
        elif self.weight < other.weight:
            return -1
        else:
            return 0
