nums = [1, 2, 3, 4]
prefixArray = [1] * len(nums)
suffixArray = [1] * len(nums)

for i in range(1, len(nums)):
    prefixArray[i] = prefixArray[i - 1] * nums[i - 1]
print(prefixArray)

for j in range(len(nums) - 2, -1, -1):
    suffixArray[j] = suffixArray[j + 1] * nums[j + 1]
print(suffixArray)
for k in range(len(nums)):
    nums[k] = prefixArray[k] * suffixArray[k]
print(nums)