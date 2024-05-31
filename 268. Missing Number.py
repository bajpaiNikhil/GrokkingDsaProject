nums = [3, 0, 1]


def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]


def cyclicSort(nums):
    i = 0
    while i < len(nums):
        if len(nums) > nums[i] != i:
            print(i, nums[i])
            swap(nums, i, nums[i])
            # temp = nums[i]  # Store the value at nums[i]
            # nums[i], nums[temp] = nums[temp], nums[i]  # Swap using temp
        else:
            i += 1


cyclicSort(nums)
print(nums)
for i in range(len(nums)):
    if i != nums[i]:
        print(i)
