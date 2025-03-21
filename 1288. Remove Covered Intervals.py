intervals = [[1, 4], [3, 6], [2, 8]]
print(len(intervals))
# intervals.sort(key = lambda x:x[0]) #[[1, 4], [2, 8], [3, 6]]
# intervals.sort(key= lambda x:(x[0],-x[1]))
# print(intervals)
intervals.sort()
x1 = intervals[0][0]
x2 = intervals[0][1]
count = 1
for i in range(1,len(intervals)):
    if intervals[i][0] > x1 and intervals[i][1]>x2:
        count+=1
    if intervals[i][1]>x2:
        x1 = intervals[i][0]
        x2 = intervals[i][1]
print(count)
