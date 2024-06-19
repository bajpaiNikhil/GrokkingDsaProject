"""
largest component
Write a function, largestComponent, that takes in the adjacency list of an undirected graph. The function should return the size of the largest connected component in the graph.

test_00:
largestComponent({
  0: ['8', '1', '5'],
  1: ['0'],
  5: ['0', '8'],
  8: ['0', '5'],
  2: ['3', '4'],
  3: ['2', '4'],
  4: ['3', '2']
}); // -> 4
test_01:
largestComponent({
  1: ['2'],
  2: ['1','8'],
  6: ['7'],
  9: ['8'],
  7: ['6', '8'],
  8: ['9', '7', '2']
}); // -> 6
test_02:
largestComponent({
  3: [],
  4: ['6'],
  6: ['4', '5', '7', '8'],
  8: ['6'],
  7: ['6'],
  5: ['6'],
  1: ['2'],
  2: ['1']
}); // -> 5
"""


def explore(nodes, currentNode, visited):

    if currentNode in visited:
        return 0
    visited.add(currentNode)
    count = 1
    for neighbour in nodes[currentNode]:
        count += explore(nodes, int(neighbour), visited)
    return count


def largestConnectedComponent(nodes):
    visited = set()
    maxCount = -1

    for node in nodes:
        #print(node)
        maxCount = max(explore(nodes, node, visited), maxCount)
    return maxCount


graph = {
    0: ['8', '1', '5'],
    1: ['0'],
    5: ['0', '8'],
    8: ['0', '5'],
    2: ['3', '4'],
    3: ['2', '4'],
    4: ['3', '2']
}
print(largestConnectedComponent(graph))
