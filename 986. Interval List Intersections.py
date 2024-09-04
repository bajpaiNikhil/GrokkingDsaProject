firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList =  [[1,5],[8,12],[15,24],[25,26]]
# [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

i = 0
j = 0
intersectionList = []
while i<len(firstList) and j <len(secondList):
    start = max(firstList[i][0], secondList[j][0])
    end = min(firstList[i][-1], secondList[j][-1])

    if start<= end:
        intersectionList.append([start,end])
    if firstList[i][-1]<secondList[j][-1]:
        i+=1
    else:
        j+=1
print(intersectionList)




# i, j, start, end = 0, 0, 0, 1
# result = []
# while i < len(firstList) and j < len(secondList):
#     aOverlapsB = secondList[j][start] <= firstList[i][start] <= secondList[j][end]
#     bOverlapsA = firstList[i][start] <= secondList[j][start] <= firstList[i][end]
#
#     if aOverlapsB or bOverlapsA:
#         result.append([max(firstList[i][start], secondList[j][start]), min(firstList[i][end], secondList[j][end])])
#
#     if firstList[i][end] < secondList[j][end]:
#         i += 1
#     else:
#         j += 1
# print(result)
