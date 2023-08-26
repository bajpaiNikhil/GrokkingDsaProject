import math

nums = [-1,2,1,-4]
target = 1

def threeSumClosest(arr,target_Sum):
    arr.sort()
    #currentDiff = math.inf
    smallestDiff = math.inf
    #
    # for traverse in range(len(nums)-2):
    #     left = traverse+1
    #     right = len(nums) - 1
    #     while left < right :



print(threeSumClosest(nums,target))