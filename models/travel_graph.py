from collections import defaultdict


class Graph(object):
    def __init__(self):
        self.graph = defaultdict(dict)
        self.vertices = set()

    def add_edge(self, x, y, distance):
        self.graph[x][y] = distance
        self.vertices.add(x)
        self.vertices.add(y)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.graph))
