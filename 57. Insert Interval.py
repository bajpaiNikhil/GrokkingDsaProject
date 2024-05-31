intervals = [[1, 3], [5, 7], [8, 12]]
newInterval = [4, 6]

i, start, end = 0, 0, 1
merged = []

while i < len(intervals) and intervals[i][end] < newInterval[start]: #intervals[i].end < newInterval.start
    merged.append(intervals[i])
    i+=1
print(merged,i)
while i < len(intervals) and intervals[i][start] <= newInterval[end]:
    newInterval[start] = min(intervals[i][start],newInterval[start])
    newInterval[end] = max(intervals[i][end], newInterval[end])
    i+=1
merged.append(newInterval)
print(newInterval)
while i < len(intervals):
    merged.append(intervals[i])
    i+=1
print(merged)


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
