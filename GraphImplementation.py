from graphviz import Digraph, Graph


class AbstractGraph:
    def __init__(self, name):
        self.nodes = []
        self.edges = []
        self.name = name

    def add_node(self, name):
        self.nodes.append(Node(name))
        self.visual.node(name)

        return

    def add_edge(self, s, d):
        self.edges.append(Edge(s, d))
        self.visual.edge(s, d)
        self.get_node(s).neighbors.append(self.get_node(d))

        return

    def get_node(self, node):
        for x in self.nodes:
            if x.name == node:
                return x
        pass

    def visualize(self):
        self.visual.render('graph.gv', cleanup=True)


class DiGraph(AbstractGraph):

    def __init__(self, name):
        super().__init__(name)
        self.visual = Digraph(comment='Directed Graph', strict=True)

    def get_t_graph(self):
        t_graph = DiGraph('t_graph')
        for node in self.nodes:
            t_graph.add_node(node.name)
        for edge in self.edges:
            t_graph.add_edge(edge.dest, edge.source)
        return t_graph


class UnDiGraph(AbstractGraph):
    def __init__(self, name):
        super().__init__(name)
        self.visual = Graph(comment='Undirected Graph', strict=True)

    def add_edge(self, s, d):
        super().add_edge(s, d)
        self.get_node(d).neighbors.append(self.get_node(s))


class Node:

    def __init__(self, name):
        self.visited = False
        self.f = None
        self.d = None
        self.p = None
        self.name = name
        self.neighbors = []
        self.color = 'white'


class Edge:

    def __init__(self, s, d):
        self.source = s
        self.dest = d
