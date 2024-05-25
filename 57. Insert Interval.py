intervals = [[1,3],[6,9]]
newInterval = [2,5]

intervals.append(newInterval)
print(intervals)
intervals.sort(key= lambda x:x[0])
print(intervals)
mergeList = []
for i in intervals:
    if not mergeList or mergeList[-1][-1]<i[0]:
        mergeList.append(i)
    else:
        mergeList[-1][-1] = max(mergeList[-1][-1],i[-1])
print(mergeList)