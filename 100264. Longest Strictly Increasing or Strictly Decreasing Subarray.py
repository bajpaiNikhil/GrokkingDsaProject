

nums = [1,10,10]

maxLength = 1
minLength = 1

ans = 1
# n = len(nums)
# # Initialize variables to keep track of the current subarray length
# inc_len, dec_len = 1, 1
# max_len = 1
#
# for i in range(1, n):
#     if nums[i] > nums[i - 1]:
#         inc_len += 1
#         dec_len = 1
#     elif nums[i] < nums[i - 1]:
#         dec_len += 1
#         inc_len = 1
#     else:
#         # Reset both lengths if the current element is equal to the previous one
#         inc_len, dec_len = 1, 1
#
#     # Update the maximum length
#     max_len = max(max_len, inc_len, dec_len)

for i in range(1,len(nums)):
    if nums[i]>nums[i-1]:
        maxLength+=1
        minLength=1
    elif nums[i]<nums[i-1]:
        maxLength=1
        minLength+=1
    else:
        maxLength,minLength = 1,1
    ans =  max(ans,maxLength,minLength)
print(ans)