


nums1 = [2,7,11,15]
nums2 = [1,10,4,11]

# sortedA = sorted(nums1)
# sortedB = sorted(nums2)
# assigned = {b:[] for b in nums2}
# remaining = []
#
# print(sortedA,sortedB,assigned)
#
# j = 0
# for a in sortedA:
#     if a > sortedB[j]:
#         assigned[sortedB[j]].append(a)
#         j+=1
#     else:
#         remaining.append(a)
# print(assigned,remaining)
# ans = []
# for b in nums2:
#     if assigned[b]:
#         ans.append(assigned[b].pop())
#     else:
#         ans.append(remaining.pop())
# print(ans)

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
