from sortedcontainers import SortedList, SortedSet, SortedDict

nums = [-3, 1, 2, -3, 0, -3]
k = 2
x = 1
result = []
sl = SortedList()

for i in range(len(nums)):
    sl.add(nums[i])
    # print(sl)
    if i - k >= 0:
        print(sl, nums[i-k],i-k)
        sl.remove(nums[i - k])
    if len(sl) >=k:
        xThValue = sl[x-1]
        if xThValue>=0:
            result.append(0)
        else:
            result.append(xThValue)
print(result)

