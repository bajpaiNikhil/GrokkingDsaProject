import math


def coinChange(coins, amount):
    def helper(target, nums, memo):
        minCount = math.inf
        if target == 0:
            return 0
        if target < 0:
            return math.inf
        if target in memo:
            return memo[target]
        for i in nums:
            numCoin = 1 + helper(target - i, nums, memo)
            minCount = min(minCount, numCoin)
        memo[target] = minCount
        return minCount

    ans = helper(amount, coins, {})
    return ans if ans != math.inf else -1


coins = [1, 2, 3]
amount = 4
print(coinChange(coins, amount))
