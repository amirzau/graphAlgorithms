from GraphImplementation import UnDiGraph, DiGraph
from graphviz import Digraph, Graph
import math


class Algorithm:
    def __init__(self, graph):
        self.graph = graph


class DFSAlgo(Algorithm):

    def __init__(self, graph):
        super().__init__(graph)
        self.time = 0

    def dfs_visit(self, u, output, c, for_ks):
        u.color = 'grey'
        self.time = self.time + 1
        u.d = self.time
        for v in u.neighbors:
            if v.color == 'white':
                v.p = u
                output.edge(u.name, v.name, label='tree', color='green')
                if for_ks:
                    c.append(v.name)
                self.dfs_visit(v, output, c, for_ks)
            elif v.color == 'grey':
                output.edge(u.name, v.name, label='back', color='blue')
            else:
                if u.d < v.d:
                    output.edge(u.name, v.name, label='forward', color='red')
                else:
                    output.edge(u.name, v.name, label='cross', color='black')

        u.color = 'black'
        self.time = self.time + 1
        u.f = self.time

    def run_algo(self, for_ks=False):
        output = Digraph(comment='DFS Algorithm', strict=True)
        output.attr(label='DFS Algorithm')
        for node in self.graph.nodes:
            output.node(node.name)
            node.color = 'white'
        self.time = 0
        ks = []
        for u in self.graph.nodes:
            if u.color == 'white':
                c = [u.name]

                self.dfs_visit(u, output, c, for_ks)
                ks.append(c)

        if for_ks:
            return ks

        output.render('DFS.gv', cleanup=True)


class BFSAlgo(Algorithm):

    def __init__(self, start, graph):
        super().__init__(graph)
        self.start = self.graph.get_node(start)

    def run_algo(self):
        output = Graph(comment='BFS Algorithm', strict=True)
        output.attr(label='BFS Algorithm')
        self.start.d = 0
        output.node(self.start.name, xlabel='0', color='blue')
        self.start.color = 'grey'
        self.start.p = None
        for node in self.graph.nodes:
            if node != self.start:
                node.color = 'white'
                node.d = math.inf
                node.p = None

        queue = [self.start]
        while queue:
            curr = queue.pop(0)
            for v in curr.neighbors:
                output.edge(curr.name, v.name)
                if v.color == 'white':
                    v.color = 'grey'
                    v.d = curr.d + 1
                    v.p = curr
                    output.node(v.name, xlabel=str(v.d))
                    queue.append(v)
            curr.color = 'black'
        output.render('BFS.gv', cleanup=True)


class KosarajuSharir(Algorithm):
    def __init__(self, graph):
        super().__init__(graph)

    def run_algo(self):
        dfs = DFSAlgo(self.graph)
        dfs.run_algo(False)
        self.graph.nodes.sort(key=lambda x: x.f, reverse=True)
        t_graph = self.graph.get_t_graph()
        dfs2 = DFSAlgo(t_graph)
        ks = dfs2.run_algo(True)
        output = Digraph(comment='output', strict=True)
        output.attr(label='Kosaraju-Sharir Algorithm')
        i = 1
        for cluster in ks:
            with output.subgraph(name=f'cluster{i}') as c:
                for n in cluster:
                    c.node(n)
                c.attr(color='red')
                c.attr(label=f'SCC_{i}')
            i = i + 1
        for edge in self.graph.edges:
            output.edge(edge.source, edge.dest)
        output.render('KS.gv', cleanup=True)
