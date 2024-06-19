"""
Write a function, arrayStepper, that takes in an array of numbers as an argument.
  You start at the first position of the array.
  The function should return a boolean indicating whether or not it is possible to
  reach the last position of the array.
  When situated at some position of the array, you may take a maximum number of
  steps based on the number at that position.

For example, given:

    idx =  0  1  2  3  4  5
numbers = [2, 4, 2, 0, 0, 1]

The answer is true.
We start at idx 0, we could take 1 step or 2 steps forward.
The correct choice is to take 1 step to idx 1.
Then take 4 steps forward to the end at idx 5.

test_00:
arrayStepper([2, 4, 2, 0, 0, 1]); // -> true
test_01:
arrayStepper([2, 3, 2, 0, 0, 1]); // -> false
test_02:
arrayStepper([3, 1, 3, 1, 0, 1]); // -> true
test_03:
arrayStepper([4, 1, 5, 1, 1, 1, 0, 4]); // -> true
test_04:
arrayStepper([4, 1, 2, 1, 1, 1, 0, 4]); // -> false
test_05:
arrayStepper([1, 1, 1, 1, 1, 0]); // -> true

"""


def arrayStepper(arr, index,memo):

    # if index in memo:
    #     return memo[index]
    # if index >= len(arr) - 1:
    #     return True
    #
    # maxStep = arr[index]
    # for step in range(1, maxStep + 1):
    #     if arrayStepper(arr, index + step, memo):
    #         memo[index] = True
    #         return True
    # memo[index] = False
    # return False
    n = len(arr)
    max_reachable = 0

    for i in range(n):
        if i > max_reachable:
            return False
        max_reachable = max(max_reachable, i + arr[i])
        if max_reachable >= n - 1:
            return True

    return False


print(arrayStepper([4, 1, 2, 1, 1, 1, 0, 4], 0,{}))
