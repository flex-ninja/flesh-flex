from shutil import which


graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m) 
    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search")

# Aim:
#   To perform BFS using python language.

# Algorithm:
#   1) Start by putting any one of the graph's vertices at the back of the queue.
#   2) Now take the graph item of the queue and add it to the visited list.
#   3) Create a list of that vertex's adjacent nodes. 
#      Add those which are not within the visited list to the rear of the queue. 
#   4) Keep continuing step two and three fill the queue is empty. 


bfs(visited, graph, '5')    # function calling
print('\n')

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '5')

# Aim:
    # To perform DFS using python language

# Algorithm:
    # 1) We will start by putting any one of the graph's vertex on top of the stack.
    # 2) After that take the top items of the stack and add it to the visited list 
    # of the vertex.
    # 3) Next, create a list of that adjacent node of the vertex. Add the ones which
    # aren't visited list or vertices to the top of the stack.
    # 4) Lastly, keep repeating steps 2 and 3 until the stack em empty.


