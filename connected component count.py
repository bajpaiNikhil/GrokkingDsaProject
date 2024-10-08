"""
connected components count
Write a function, connectedComponentsCount, that takes in the adjacency list of an undirected graph. The function should return the number of connected components within the graph.

test_00:
connectedComponentsCount({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}); // -> 2
test_01:
connectedComponentsCount({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
}); // -> 1
test_02:
connectedComponentsCount({
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
}); // -> 3
"""


def exploreGraph(graph, currentNode, visitedSet):
    if currentNode in visitedSet:
        return False
    visitedSet.add(currentNode)
    for neighbour in graph[currentNode]:
        exploreGraph(graph, neighbour, visitedSet)
    return True


def connectedComponentsCount(graph):
    visitedSet = set()
    count = 0
    for node in graph:
        if exploreGraph(graph, node, visitedSet):
            count += 1
    return count


graph = {
    3: [],
    4: [6],
    6: [4, 5, 7, 8],
    8: [6],
    7: [6],
    5: [6],
    1: [2],
    2: [1]
}
print(connectedComponentsCount(graph))
