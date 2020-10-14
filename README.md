# graphAlgorithms
a collection of graph algorithms - visualised in pdf



* to create a regular graph - use the UnDiGraph class
* to create a directed graph - use the DiGraph class
* to visualize the graph - use: (graphs name).visualize
* to add a node - use: (graphs name).add_node(name of the node)
* to add an edge - use : (graphs name).add_edge(name of source node, name of destination node)



* to run an algorithm:
- create an instance of the algorithm with the desirable graph (in case of BFS - also pass the start node's name)
- instance.run_algo()
- a pdf file will be generated into the projects folder.

**examples are in main.py**

****note****
BFS will work only on regular graphs.
DFS and KS will work only on directed graphs.
