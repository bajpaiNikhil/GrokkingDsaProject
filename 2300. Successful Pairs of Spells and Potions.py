spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7


potions.sort()
res= []
for spell in spells:
    #insert binary search
    left , right = 0 , len(potions)-1
    ans = len(potions)
    while left <= right:
        mid = left + (right-left)//2
        if potions[mid]* spell >= success :
            ans = mid
            right = mid-1
        else:
            left = mid+1
    res.append(len(potions)-ans)
print(res)