graph = {
'A':[('B',12), ('C',4)],
'B':[('D',7), ('E',3)],
'C':[('F',8), ('G',2)],
'D':[],
'E':[('H',0)],
'F':[('H',0)],
'G':[('H',0)]
}
def bestfirstsearch(start, target, graph, queue=[], visited=[]):
    if start not in visited:
        print(start)
        visited.append(start)
    queue=queue+[x for x in graph[start] if x[0][0] not in visited]
    queue.sort(key=lambda x:x[1])
    if queue[0][0]==target:
        print(queue[0][0])
    else:
        processing=queue[0]
        queue.remove(processing)
        bestfirstsearch(processing[0], target, graph, queue, visited)
bestfirstsearch('A', 'H', graph)

# Aim:
#     To perform Best First Search algorithm in AWS platform.
# Algorithm:
#     1) Place the starting node into the open list.
#     2) If the open list es empty, stop and return failure.
#     3) Remove the node n, from the open list which has lower value of n(n)
#     and generate the successors of node n.
#     4) Check each successor of node n and find whether any node is in good node or not.
#     5) For each successor node and then check if node has been an either open or closed
#     list. If the node has not been in both list then add it to open list. 
#     6) Return to step 2 tell final node has reached.
