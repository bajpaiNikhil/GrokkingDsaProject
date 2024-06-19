nums =  [0,3,7,2,5,8,4,6,0,1]
hashSet = set(nums)
longest = 0
for i in nums:
    if i-1 not in hashSet:
        length = 0
        while i + length in hashSet:
            length+=1
        longest = max(longest,length)
print(longest)