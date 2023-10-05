


nums1 = [2,7,11,15]
nums2 = [1,10,4,11]

sortedNums2 = sorted([(num,i) for i,num in enumerate(nums2)])[::-1]
sortedNums1 = sorted(nums1)[::-1]
print(sortedNums1,sortedNums2)
left = 0
right = len(nums1)-1
res = [-1]* len(nums1)
for num,index in sortedNums2:
    print(num,index)
    if sortedNums1[left] > num:
        res[index] = sortedNums1[left]
        left +=1
    else :
        res[index] = sortedNums1[right]
        right -=1
print(res)
