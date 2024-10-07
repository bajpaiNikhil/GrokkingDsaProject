

n = 5
corridors = [[1,2]
,[2,3]
,[3,4]
,[1,3]
,[4,5]
,[1,5]
,[1,4]]


def intersectionOf2Rooms(neigbourOfNode1, neigbourOfNode2):
    count = 0
    for i in neigbourOfNode1:
        if i in neigbourOfNode2:
            count+=1
    return count


def numberOfCyclicPath(corridors,n):
    graph = {}
    cycle = 0
    for edge in corridors:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
        neigbourOfNode1 = graph[a]
        neigbourOfNode2 = graph[b]
        print(neigbourOfNode2,neigbourOfNode1)
        cycle+= intersectionOf2Rooms(neigbourOfNode1,neigbourOfNode2)
    return cycle

print(numberOfCyclicPath(corridors,n))