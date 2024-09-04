intervals = [[1, 3], [15, 18],[2, 6], [8, 10]]
# [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals.sort(key=lambda  x: x[0])
print(intervals)
result = [intervals[0]]
print(result)
for interval in range(1,len(intervals)):
    print(intervals[interval])
    if not result or result[-1][-1]<intervals[interval][0]:
        result.append(intervals[interval])
    else:
        result[-1][-1] = max(intervals[interval][-1],result[-1][-1])
print(result)
# intervals.sort(key=lambda x: x[0])
# # print(intervals)
# mergeList = []
# for i in intervals:
#     # if the list of merged intervals is empty
#     # or if the current interval does not overlap with the previous,
#     # simply append it.
#     if not mergeList or mergeList[-1][-1] < i[0]:
#         mergeList.append(i)
#     else:
#         mergeList[-1][-1] = max(mergeList[-1][-1], i[-1])
# print(mergeList)
