# graph = {
# 'A':[('B',12), ('C',4)],
# 'B':[('D',7), ('E',3)],
# 'C':[('F',8), ('G',2)],
# 'D':[],
# 'E':[('H',0)],
# 'F':[('H',0)],
# 'G':[('H',0)]
# }

graph={
    '0':[('1',3),('2',6),('3',5)],
    '1':[('4',9),('5',8)],
    '2':[('6',12),('7',14)],
    '3':[('8',7)],
    '8':[('9',5),('10',6)],
    '9':[('11',1),('12',10),('13',2)]
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
        
        
        
bestfirstsearch('0','9', graph)