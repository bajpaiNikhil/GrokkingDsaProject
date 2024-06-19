"""
Question : sum possible
Write a function sumPossible that takes in an amount and an array of positive numbers.
 The function should return a boolean indicating whether or not it is possible to
  create the amount by summing numbers of the array.
   You may reuse numbers of the array as many times as necessary.

You may assume that the target amount is non-negative.

test_00:
sumPossible(8, [5, 12, 4]); // -> true, 4 + 4
test_01:
sumPossible(15, [6, 2, 10, 19]); // -> false
test_02:
sumPossible(13, [6, 2, 1]); // -> true
test_03:
sumPossible(103, [6, 20, 1]); // -> true
test_04:
sumPossible(12, []); // -> false
test_05:
sumPossible(12, [12]); // -> true

"""


def findSum(target, arr, memo):
    if target == 0: return True

    if target < 0: return False

    if target in memo: return memo[target]

    for i in arr:
        if findSum(target - i, arr, memo):
            memo[target] = True
            return True
    memo[target] = False
    return False


print(findSum(8, [5, 12, 4], {}))
print(findSum(15, [6, 2, 10, 19], {}))
print(findSum(13, [6, 2, 1], {}))
print(findSum(103, [6, 20, 1], {}))
print(findSum(12, [], {}))
