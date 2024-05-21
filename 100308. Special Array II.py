nums = [4,3,1,6]
queries = [[0,2],[2,3]]
j = 0
convertedArray = []
ans = []
converted = [0]
for i in range(1, len(nums)):
    if nums[i] % 2 == nums[i - 1] % 2:
        j += 1
    converted.append(j)
for q in queries:
    ans.append(converted[q[0]] == converted[q[1]])
print(ans,converted)
