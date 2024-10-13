from collections import Counter

nums = [3, 8, 7, 8, 7, 5]
k = 2
x = 2
result = []
for i in range(len(nums) - k + 1):
    # print(nums[i:i+k])
    subArray = nums[i:i + k]
    frequency = Counter(subArray)
    # print(frequency)
    sorted_frequency = sorted(frequency.items(), key=lambda item: (-item[1], -item[0]))
    # print(sorted_frequency)
    subArray_sum = 0
    elementCount = 0
    for emt, cont in sorted_frequency:
        if elementCount >= x:
            break
        subArray_sum += emt * cont
        elementCount += 1
    result.append(subArray_sum)
print(result)
