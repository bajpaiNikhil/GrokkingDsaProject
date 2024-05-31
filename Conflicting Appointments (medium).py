

intervals = [[1,100],[11,22],[1,11],[2,12]]
# [[1, 100], [1, 11], [2, 12], [11, 22]]
intervals.sort(key=lambda x:x[1])
print(intervals)
start , end = 0,1
count = 0
res = []
for i in range(len(intervals)):
    if res and intervals[i][start]<res[-1][end]:
        count+=1
    else:
        res.append(intervals[i])
print(count)