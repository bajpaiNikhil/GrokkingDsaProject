nums = [0, -3, 5, -1, 7, -2, -4, 1, 3]

hashSet = set(nums)
print(hashSet)
ans = 0
for i in range(len(nums)):
    if nums[i]-1 not in hashSet:
        chainLength=1
        x = nums[i]+1
        while x in hashSet:
            chainLength+=1
            x+=1
        # print(hashSet)
        ans=max(ans,chainLength)
print(ans)