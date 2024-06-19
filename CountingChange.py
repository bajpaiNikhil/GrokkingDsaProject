"""
Write a function, countingChange, that takes in an amount and an array of coins. The function should return the number of different ways it is possible to make change for the given amount using the coins.

You may reuse a coin as many times as necessary.

For example,

countingChange(4, [1,2,3]) -> 4

There are four different ways to make an amount of 4:

1. 1 + 1 + 1 + 1
2. 1 + 1 + 2
3. 1 + 3
4. 2 + 2
test_00:
countingChange(4, [1, 2, 3]); // -> 4
test_01:
countingChange(8, [1, 2, 3]); // -> 10
test_02:
countingChange(24, [5, 7, 3]); // -> 5
"""


def countingChange(nums, amount, i,memo):
    key = f"{amount},{i}"
    if key in memo:
        return memo[key]
    if amount == 0:
        return 1
    if i == len(nums):
        return 0
    coin = nums[i]
    quantity = 0
    totalCoin = 0
    while quantity * coin <= amount:
        remainder = amount - (quantity * coin)
        totalCoin += countingChange(nums, remainder, i + 1,memo)
        quantity += 1
    memo[key] = totalCoin
    return totalCoin


print(countingChange([1, 2, 3], 4,0,{}))
