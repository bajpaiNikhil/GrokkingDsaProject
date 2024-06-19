"""
longest path
Write a function, longestPath, that takes in an adjacency list for a directed acyclic graph.
The function should return the length of the longest path within the graph. A path may start and end at any two nodes.
The length of a path is considered the number of edges in the path, not the number of nodes.

test_00:
const graph = {
  a: ['c', 'b'],
  b: ['c'],
  c: []
};

longestPath(graph); // -> 2
test_01:
const graph = {
  a: ['c', 'b'],
  b: ['c'],
  c: [],
  q: ['r'],
  r: ['s', 'u', 't'],
  s: ['t'],
  t: ['u'],
  u: []
};

longestPath(graph); // -> 4
"""


def traverseDistance(graph, node, distance):
    if node in distance:
        return distance[node]
    maxLength = 0
    for neighbour in graph[node]:
        attempt = traverseDistance(graph, neighbour, distance)
        maxLength = max(attempt, maxLength)
    distance[node] = 1 + maxLength
    return 1 + maxLength


def longestPath(graph):
    distance = {}
    for node in graph:
        if len(graph[node]) == 0:
            distance[node] = 0
    for node in graph:
        traverseDistance(graph, node, distance)
    return max(distance.values())


graph = {
    "a": ['c', 'b'],
    "b": ['c'],
    "c": [],
}
print(longestPath(graph))
