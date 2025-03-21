intervals = [[1,5]]
newInterval = [2,3]

i = 0
currentIntervalsLength = len(intervals)
result = []
# Step1 = Since the intervals are sorted, we'll create an empty list,
# output,and start adding the intervals that start before the new interval.
while i < currentIntervalsLength and intervals[i][0] < newInterval[0]:
    result.append(intervals[i])
    i += 1

print(result)
# Next, we'll add the new interval to the output list and merge
# it with the previously added interval if there is an overlap.
if len(result) == 0 or result[-1][-1] < newInterval[0]:
    result.append(newInterval)
else:
    result[-1][-1] = max(newInterval[-1], result[-1][-1])
print(result)
# Finally, we'll add the remaining intervals to the output list,
# merging them with the previously added intervals when they overlap.
while i < currentIntervalsLength:
    if result[-1][-1] < intervals[i][0]:
        result.append(intervals[i])
    else:
        result[-1][-1] = max(intervals[i][-1], result[-1][-1])
    i+=1
print(result)
# i, start, end = 0, 0, 1
# merged = []
#
# while i < len(intervals) and intervals[i][end] < newInterval[start]: #intervals[i].end < newInterval.start
#     merged.append(intervals[i])
#     i+=1
# print(merged,i)
# while i < len(intervals) and intervals[i][start] <= newInterval[end]:
#     newInterval[start] = min(intervals[i][start],newInterval[start])
#     newInterval[end] = max(intervals[i][end], newInterval[end])
#     i+=1
# merged.append(newInterval)
# print(newInterval)
# while i < len(intervals):
#     merged.append(intervals[i])
#     i+=1
# print(merged)


# intervals.append(newInterval)
# print(intervals)
# intervals.sort(key= lambda x:x[0])
# print(intervals)
# mergeList = []
# for i in intervals:
#     if not mergeList or mergeList[-1][-1]<i[0]:
#         mergeList.append(i)
#     else:
#         mergeList[-1][-1] = max(mergeList[-1][-1],i[-1])
# print(mergeList)
