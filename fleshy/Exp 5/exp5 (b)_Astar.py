#A*
from hashlib import algorithms_available


def aStarAlgo(start_node, stop_node):
         
        open_set = set(start_node) 
        closed_set = set()
        g = {}
        parents = {}

        g[start_node] = 0
        parents[start_node] = start_node
         
         
        while len(open_set) > 0:
            n = None
            for v in open_set:
                if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                    n = v
             
                     
            if n == stop_node or Graph_nodes[n] == None:
                pass
            else:
                for (m, weight) in get_neighbors(n):
                    if m not in open_set and m not in closed_set:
                        open_set.add(m)
                        parents[m] = n
                        g[m] = g[n] + weight

                    else:
                        if g[m] > g[n] + weight:
                            g[m] = g[n] + weight
                            parents[m] = n
                             
                            if m in closed_set:
                                closed_set.remove(m)
                                open_set.add(m)
 
            if n == None:
                print('Path does not exist!')
                return None

            if n == stop_node:
                path = []
 
                while parents[n] != n:
                    path.append(n)
                    n = parents[n]
 
                path.append(start_node)
 
                path.reverse()
 
                print('{}'.format(path))
                return path
            open_set.remove(n)
            closed_set.add(n)
 
        print('Path does not exist!')
        return None
         

def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None


def heuristic(n):
        H_dist = {
            'S': 5,
            'A': 3,
            'B': 4,
            'C': 2,
            'D': 6,
            'G': 0,
             
        }
 
        return H_dist[n]
 

Graph_nodes = {
    'S': [('A', 1),('G', 10)],
    'A': [('B', 2),('C', 1)],
    'C': [('G', 4),('D', 3)],
    'B': [('D', 2)],
    'D': [('G', 2)],
}

aStarAlgo('S', 'G')


# Aim:
#     To implement A* algorithm

# Algorithm:
#     1) Define list open.
#     2) If list is empty, return failure and exit.
#     3)  a) Remove node n with smallest value of f(n) from open and move it to closed list.
#         b)If the node n is goal state return success and exit. 
#     4) Expand node n. 
#     5) Perform same for the successor nodes. 
#     6) Apply function to the nodes. 
#     7) Return to step 2. 
#     8) Exit. 