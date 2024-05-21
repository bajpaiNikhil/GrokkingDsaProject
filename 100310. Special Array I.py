nums = [4,3,1,6]
k = 2

windowStart = 0
flag = False
for i in range(len(nums)):
    if (i - windowStart + 1) == k:
        print(nums[i], nums[windowStart])
        if (nums[i] % 2 == 0 and nums[windowStart] % 2 != 0) or (nums[windowStart] % 2 == 0 and nums[i] % 2 != 0):
            flag = True
            print(True, nums[i], nums[windowStart])
        else:

            print(False,nums[i], nums[windowStart])
        windowStart += 1
