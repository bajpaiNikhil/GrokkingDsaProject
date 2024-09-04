import collections


def runningDfs(adjList, src, dst,visited):
    if src in visited:
        return True
    visited.add(src)
    if src == dst:
        return True
    for neighbour in adjList[src]:
        if neighbour not in visited:
            if runningDfs(adjList, neighbour, dst, visited):
                return True
    return False


def hasAPath(edges, source, destination):

    adjList = collections.defaultdict(list)
    for edge in edges:
        a,b = edge
        adjList[a].append(b)
        adjList[b].append(a)
    print(adjList)
    return runningDfs(adjList,source,destination,set())
n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source = 0
destination = 2
print(hasAPath(edges,source , destination))