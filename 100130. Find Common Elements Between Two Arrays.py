nums1 =  [3,4,2,3]
nums2 = [8,6]
set1 = set(nums1)
set2 = set(nums2)

common_in_nums2 = sum(1 for num in nums1 if num in set2)
common_in_nums1 = sum(1 for num in nums2 if num in set1)

print([common_in_nums2, common_in_nums1])
