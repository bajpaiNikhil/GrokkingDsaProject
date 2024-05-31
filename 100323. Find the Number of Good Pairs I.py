nums1 = [1,3,4]
nums2 = [1,3,4]
k = 1

# nums2 = [i*k for i in nums2]
# print(nums2)
count = 0
for i in nums1:
    for j in nums2:
        if i%(j*k) == 0:
            count +=1
print(count)