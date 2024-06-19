"""
prereqs possible
Write a function, prereqsPossible, that takes in a number of courses (n) and prerequisites as arguments. Courses have ids ranging from 0 through n - 1. A single prerequisite of [A, B] means that course A must be taken before course B. The function should return a boolean indicating whether or not it is possible to complete all courses.

test_00:
const numCourses = 6;
const prereqs = [
  [0, 1],
  [2, 3],
  [0, 2],
  [1, 3],
  [4, 5],
];
prereqsPossible(numCourses, prereqs); // -> true
test_01:
const numCourses = 6;
const prereqs = [
  [0, 1],
  [2, 3],
  [0, 2],
  [1, 3],
  [4, 5],
  [3, 0],
];
prereqsPossible(numCourses, prereqs); // -> false
test_02:
const numCourses = 5;
const prereqs = [
  [2, 4],
  [1, 0],
  [0, 2],
  [0, 4],
];
prereqsPossible(numCourses, prereqs); // -> true
test_03:
const numCourses = 6;
const prereqs = [
  [2, 4],
  [1, 0],
  [0, 2],
  [0, 4],
  [5, 3],
  [3, 5],
];
prereqsPossible(numCourses, prereqs); // -> false
test_04:
const numCourses = 8;
const prereqs = [
  [1, 0],
  [0, 6],
  [2, 0],
  [0, 5],
  [3, 7],
  [4, 3],
];
prereqsPossible(numCourses, prereqs); // -> true
"""


def buildGraph(numCourses, preregs):
    graph = {}
    for node in range(numCourses):
        graph[node] = []

    for i in preregs:
        a, b = i
        graph[a].append(b)
    return graph


def cycleDetection(graph, node, visiting, visited):
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


def preregsPossible(numCourses, preregs):
    graph = buildGraph(numCourses, preregs)

    visiting = set()
    visited = set()
    for node in graph:
        if cycleDetection(graph,node,visiting,visited):
            return False
    return True


numCourses = 6
prereqs = [
    [0, 1],
    [2, 3],
    [0, 2],
    [1, 3],
    [4, 5],
]

print(preregsPossible(numCourses,prereqs))
