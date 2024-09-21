def swappedNums(nums, i, j):
    numsSwapped = nums
    numsSwapped[i], numsSwapped[j] = numsSwapped[j], numsSwapped[i]
    return numsSwapped


def findAllPermutation(nums, currentIndex, results):
    if currentIndex == len(nums) - 1:
        results.append(nums[:])
        return results
    for i in range(currentIndex, len(nums)):
        swapped = swappedNums(nums, currentIndex, i)
        print(swapped)
        findAllPermutation(swapped, currentIndex + 1, results)
        swappedNums(nums, currentIndex, i)


def permutationAre(nums):
    results = []
    findAllPermutation(nums, 0, results)
    return results


nums = [1, 2, 3]
print(permutationAre(nums))
