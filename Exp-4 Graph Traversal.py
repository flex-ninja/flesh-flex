graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}



def bfs(graph, node): #function for BFS
  visitedBFS = [] # List for visited nodes.
  queue = []     #Initialize a queue
  visitedBFS.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visitedBFS:
        visitedBFS.append(neighbour)
        queue.append(neighbour)
        

visitedDFS = set() # Set to keep track of visited nodes of graph

def dfs(visitedDFS, graph, node):  #function for dfs 
    if node not in visitedDFS:
        print (node, end=" ")
        visitedDFS.add(node)
        for neighbour in graph[node]:
            dfs(visitedDFS, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visitedDFS, graph, '5')

print()

# Driver Code
print("Following is the Breadth-First Search")
bfs( graph, '5')    # function calling