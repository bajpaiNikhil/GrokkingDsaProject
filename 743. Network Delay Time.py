import heapq
from collections import defaultdict

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2

def networkDelay(times,n,k):
    graph = defaultdict(list)
    for sourceNode,targetNode,time in times:
        graph[sourceNode].append((targetNode,time))
    print(graph)
    priorityQueue = [(0,k)]
    visited= set()
    delayTimeIs = 0
    while priorityQueue:
        timeIs,currentNode = heapq.heappop(priorityQueue)
        # print(timeIs,currentNode)
        if currentNode in visited:
            continue
        visited.add(currentNode)
        delayTimeIs = max(delayTimeIs,timeIs)
        for neighbour, neighbourTime in graph[currentNode]:
            if neighbour not in visited:
                heapq.heappush(priorityQueue,(neighbourTime+timeIs,neighbour))

    return delayTimeIs if len(visited) == n else -1

print(networkDelay(times,n,k))