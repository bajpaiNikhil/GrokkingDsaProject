nums = [2,5,6,8,5]
k = 7

print(sum(nums)//len(nums))
print(sum([2, 7, 7, 8, 5])//len(nums))

left = 0
right = 10**6
ans = 0
#
#
# def check(nums, k, mid):
#
#     current_mean = sum(nums)//len(nums)
#     while mid >0:
#         if current_mean > k:
#             a = nums.index(max(nums))
#             nums[a]-=1
#         else:
#             a = nums.index(max(nums))
#             nums[a] -= 1
#         mean = sum(nums)//len(nums)
#         if mean == k:
#             return True
#     return False
#
# while left <= right :
#     mid = left +(right - left)//2
#
#     if check(nums,k , mid):
#         ans = mid
#         right = mid-1
#     else:
#         left = mid+1
# print(ans)