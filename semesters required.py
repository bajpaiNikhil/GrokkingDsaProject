"""
semesters required
Write a function, semestersRequired, that takes in a number of courses (n) and a list of prerequisites as arguments.
Courses have ids ranging from 0 through n - 1. A single prerequisite of [A, B] means that course A must be taken before
course B. Return the minimum number of semesters required to complete all n courses.
There is no limit on how many courses you can take in a single semester,
as long the prerequisites of a course are satisfied before taking it.

Note that given prerequisite [A, B], you cannot take course A and course B concurrently in the same semester.
You must take A in some semester before B.

You can assume that it is possible to eventually complete all courses.

test_00:
const numCourses = 6;
const prereqs = [
  [1, 2],
  [2, 4],
  [3, 5],
  [0, 5],
];
semestersRequired(numCourses, prereqs); // -> 3
test_01:
const numCourses = 7;
const prereqs = [
  [4, 3],
  [3, 2],
  [2, 1],
  [1, 0],
  [5, 2],
  [5, 6],
];
semestersRequired(numCourses, prereqs); // -> 5
test_02:
const numCourses = 5;
const prereqs = [
  [1, 0],
  [3, 4],
  [1, 2],
  [3, 2],
];
semestersRequired(numCourses, prereqs); // -> 2
test_03:
const numCourses = 12;
const prereqs = [];
semestersRequired(numCourses, prereqs); // -> 1
"""


def buildGraph(numCourses,preregs):
    graph = {}
    for i in range(numCourses):
        graph[i] = []
    for node in preregs:
        a, b = node
        graph[a].append(b)
    return graph


def traverseDistance(graphs, node, distance):
    if node in distance:
        return distance[node]
    maxAttempt = 0
    for neighbour in graphs[node]:
        attempt = traverseDistance(graphs,neighbour,distance)
        maxAttempt = max(attempt,maxAttempt)
    distance[node] = 1+maxAttempt
    return maxAttempt+1


def semestersRequired(numCourses, preregs):
    graphs = buildGraph(numCourses,preregs)
    distance = {}
    for node in graphs:
        if len(graphs[node]) == 0:
            distance[node] = 1
    for node in graphs:
        traverseDistance(graphs,node,distance)
    print(graphs)
    return max(distance.values())


numCourses = 15
prereqs = [

]
print(semestersRequired(numCourses, prereqs))
