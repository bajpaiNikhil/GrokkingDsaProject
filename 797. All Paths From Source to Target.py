import collections

graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]


def dfs(pathList, graph, vertix, finalList):
    pathList.append(vertix)
    if vertix == len(graph) - 1:
        finalList.append(pathList[:])
    else:
        for neighbour in graph[vertix]:
            if neighbour not in pathList:  # To avoid cycles
                dfs(pathList, graph, neighbour, finalList)
    pathList.pop()  # Backtrack to explore other paths
    return finalList

def findAllPathBetweenFirstAndLastNode(graph):
    result = []
    pathList = []
    return dfs(pathList, graph, 0, result)


print(findAllPathBetweenFirstAndLastNode(graph))
