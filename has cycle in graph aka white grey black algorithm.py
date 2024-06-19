"""
has cycle
Write a function, hasCycle, that takes in an object representing the adjacency list of a directed graph.
The function should return a boolean indicating whether or not the graph contains a cycle.

test_00:
hasCycle({
  a: ["b"],
  b: ["c"],
  c: ["a"],
}); // -> true
test_01:
hasCycle({
  a: ["b", "c"],
  b: ["c"],
  c: ["d"],
  d: [],
}); // -> false
test_02:
hasCycle({
  a: ["b", "c"],
  b: [],
  c: [],
  e: ["f"],
  f: ["e"],
}); // -> true
test_03:
hasCycle({
  q: ["r", "s"],
  r: ["t", "u"],
  s: [],
  t: [],
  u: [],
  v: ["w"],
  w: [],
  x: ["w"],
}); // -> false
"""
def cycleDetection(graph , node , visiting , visited):
    if node in visited:
        return False
    if node in visiting:
        return True
    visiting.add(node)
    for neighbour in graph[node]:
        if cycleDetection(graph,neighbour,visiting,visited):
            return True
    visiting.remove(node)
    visited.add(node)
    return False

def hasCycle(graph):
    visiting = set()
    visited = set()
    for node in graph:
        if cycleDetection(graph,node,visiting,visited):
            return True
    return False

graph = {
  "a": ["b", "c"],
  "b": ["c"],
  "c": ["d"],
  "d": [],
}
print(hasCycle(graph))