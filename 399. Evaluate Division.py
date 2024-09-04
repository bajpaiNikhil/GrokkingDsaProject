import collections


def runBfs(src, target, adjList):
    if src not in adjList or target not in adjList:
        return -1

    queue, visited = collections.deque(), set()
    queue.append([src, 1])
    visited.add(src)
    while queue:
        node, weight = queue.popleft()
        if node == target:
            return weight
        for nextNode, nextWeight in adjList[node]:
            if nextNode not in visited:
                queue.append([nextNode, weight * nextWeight])
                visited.add(nextNode)
    return -1


def Evaluate(equations, values, queries):
    adjList = collections.defaultdict(list)
    for idx, eq in enumerate(equations):
        # print(eq,idx)
        a, b = eq
        adjList[a].append([b, values[idx]])
        adjList[b].append([a, 1 / values[idx]])
    print(adjList)
    return [runBfs(q[0], q[1] ,adjList) for q in queries]


equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
print(Evaluate(equations, values, queries))
