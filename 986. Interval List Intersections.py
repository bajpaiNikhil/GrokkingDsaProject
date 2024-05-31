firstList = [[1, 10]]
secondList = [[3, 7]]
# [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
i, j, start, end = 0, 0, 0, 1
result = []
while i < len(firstList) and j < len(secondList):
    aOverlapsB = secondList[j][start] <= firstList[i][start] <= secondList[j][end]
    bOverlapsA = firstList[i][start] <= secondList[j][start] <= firstList[i][end]

    if aOverlapsB or bOverlapsA:
        result.append([max(firstList[i][start], secondList[j][start]), min(firstList[i][end], secondList[j][end])])

    if firstList[i][end] < secondList[j][end]:
        i += 1
    else:
        j += 1
print(result)
