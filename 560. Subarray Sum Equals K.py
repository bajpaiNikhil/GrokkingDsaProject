nums = [1,-1,3,2,-2,-8,1,7,10,23]
prefixSumArray = [nums[0]]
d = {0: -1}
# sumIs = 0
ans = 0
for i in range(1,len(nums)):
    prefixSumArray.append((prefixSumArray[-1]+nums[i]))
print(prefixSumArray)

for i in range(len(prefixSumArray)):
    if prefixSumArray[i] not in d:
        d[prefixSumArray[i]] = i
    else:
        ans = max(ans, i - d[prefixSumArray[i]])
        # print(ans)
print(ans)
