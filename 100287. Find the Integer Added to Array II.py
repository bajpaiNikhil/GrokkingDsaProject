nums1 =  [3,5,5,3]
nums2 = [7,7]
# nums1.sort()
# nums2.sort()
print(nums1, nums2)
minList = []
for i in range(len(nums1) - len(nums2) + 1):
    # print(nums1[i:len(nums2) + i])
    a = nums1[i:len(nums2) + i]
    b = nums2
    l = 1
    r = 1
    ans = b[0] - a[0]
    while l != len(a) and r != len(b):
        diff = b[r] - a[l]
        l += 1
        r += 1
        if diff == ans:
            continue
        else:
            break
    minList.append(ans)
print(min(minList))
# a = [8, 12, 16]
# b = [10, 14, 18]
# l = 1
# r = 1
# ans = b[0] - a[0]
# while  l!=len(a) and r != len(b):
#     diff = b[r] - a[l]
#     l += 1
#     r += 1
#     if diff == ans:
#         continue
#     else:
#         break
# print(ans)



