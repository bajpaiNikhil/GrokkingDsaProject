import collections


def checkForIncomingAndOutgoingEdges(trust):
    hashMapForIncomingEdges = collections.defaultdict(int)
    hashMapForOutgoingEdges = collections.defaultdict(int)

    for tst in trust:
        outgoing, incoming = tst[0], tst[1]
        hashMapForOutgoingEdges[outgoing] += 1
        hashMapForIncomingEdges[incoming] += 1
    print(hashMapForOutgoingEdges,hashMapForIncomingEdges)
    for i in range(1,n+1):
        if hashMapForOutgoingEdges[i] == 0 and hashMapForIncomingEdges[i] == n-1:
            return i
    return -1

n = 3
trust = [[1, 3], [2, 3]]
print(checkForIncomingAndOutgoingEdges(trust))
