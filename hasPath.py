from collections import deque

"""
has path
Write a function, hasPath, that takes in an object representing the adjacency list of a directed acyclic graph and two nodes (src, dst). The function should return a boolean indicating whether or not there exists a directed path between the source and destination nodes.

Hey. This is our first graph problem, so you should be liberal with watching the Approach and Walkthrough. Be productive, not stubborn. -AZ

test_00:
const graph = {
  f: ['g', 'i'],
  g: ['h'],
  h: [],
  i: ['g', 'k'],
  j: ['i'],
  k: []
};

hasPath(graph, 'f', 'k'); // true
test_01:
const graph = {
  f: ['g', 'i'],
  g: ['h'],
  h: [],
  i: ['g', 'k'],
  j: ['i'],
  k: []
};

hasPath(graph, 'f', 'j'); // false
test_02:
const graph = {
  f: ['g', 'i'],
  g: ['h'],
  h: [],
  i: ['g', 'k'],
  j: ['i'],
  k: []
};

hasPath(graph, 'i', 'h'); // true
"""


def hasPathWithDFS(graph, src, dst):
    if src == dst:
        return True

    for neighbour in graph[src]:
        if hasPathWithDFS(graph, neighbour, dst):
            return True
    return False


def hasPathWithBFS(graph, src, dst):
    queue = deque(src)
    while len(queue) > 0:
        currentNode = queue.popleft()
        if currentNode == dst:
            return True
        for neighbour in graph[currentNode]:
            queue.append(neighbour)
    return False


graph = {
    "f": ['g', 'i'],
    "g": ['h'],
    "h": [],
    "i": ['g', 'k'],
    "j": ['i'],
    "k": []
}
print(hasPathWithBFS(graph, "f", "k"))
print(hasPathWithDFS(graph, "f", "k"))