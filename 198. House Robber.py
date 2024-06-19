def houseRobber(nums):
    def helper(arr, i, memo):
        if i >= len(arr): return 0
        if i in memo:
            return memo[i]

        include = arr[i] + helper(arr, i + 2, memo)
        exclude = helper(arr, i + 1, memo)

        memo[i] = max(include, exclude)
        return memo[i]

    return helper(nums, 0, {})


nums = [2, 7, 9, 3, 1]
print(houseRobber(nums))
