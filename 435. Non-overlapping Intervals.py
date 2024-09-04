intervals = [[1,2],[2,3],[3,4],[1,3]]
intervals.sort(key= lambda x: x[0])
count = 0
print(intervals)
res =[]
for i in range(len(intervals)):
    if res and intervals[i][0] < res[-1][-1]:
        print(res, "1" ,intervals[i], "2", res[-1])
        count+=1
    else:
        res.append(intervals[i])
print(count)