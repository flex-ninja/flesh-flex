from xml.dom.minicompat import NodeList
from cv2 import Algorithm
from matplotlib.style import available


class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
 
        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
 
# Function to assign colors to vertices of a graph
def colorGraph(graph, n):
 
    # keep track of the color assigned to each vertex
    result = {}
 
    # assign a color to vertex one by one
    for u in range(n):
 
        # check colors of adjacent vertices of `u` and store them in a set
        assigned = set([result.get(i) for i in graph.adjList[u] if i in result])
 
        # check for the first free color
        color = 1
        for c in assigned:
            if color != c:
                break
            color = color + 1
 
        # assign vertex `u` the first available color
        result[u] = color
 
    for v in range(n):
        print(f'Color assigned to vertex {v} is {colors[result[v]]}')
 
 
# Greedy coloring of a graph
if __name__ == '__main__':
 
    # Add more colors for graphs with many more vertices
    colors = ['', 'RED', 'YELLOW', 'BLUE', 'GREEN', 'PURPLE', 'PINK',
            'BLACK', 'BROWN', 'WHITE', 'ORANGE', 'VOILET']
 
    # List of graph edges as per the above diagram
    edges = [(0, 1), (0, 2), (1, 5), (2, 5), (2, 4), (2, 3), (0, 3), (1, 4), (0,5)]
 
    # total number of nodes in the graph (labelled from 0 to 5)
    n = 6
 
    # build a graph from the given edges
    graph = Graph(edges, n)
 
    # color graph using the greedy algorithm
    colorGraph(graph, n)

# Aim:
#     To solve and perform graph coloring for vertex coloring.
# Algorithm:
#     a)Vertex Coloring:

#     (i)Add a list of colors for graph.
#     (ii)Then give list of graph edges and nodes 
#     and create a function to build a graph from 
#     those edges.
#     (iii)Add and convert edges to unidirected graph 
#     (iv)Create a function to assign colors to vertices
#     of a graph. 
#     (v)Check for the first free color and assign a color 
#     to vertex one by one.
#     (vi)Check colors of adjacent vertices of 'u' and 
#     store them in a set, after checking assign vertex
#     'u' the first available color.
#     (vii)After processing all vertex, print the output.
