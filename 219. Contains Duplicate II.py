
nums = [1,2,3,4,1]
k = 3
sets = set()
for i,j in enumerate(nums):
    print(i,j)
    if j in sets:
        print(True)
        break
    sets.add(j)
    print(sets)
    if len(sets) > k:
        print(sets,"with length",nums[i-k],i,j,len(sets))
        sets.remove(nums[i-k])
    #sets.add(j)
print(False)
