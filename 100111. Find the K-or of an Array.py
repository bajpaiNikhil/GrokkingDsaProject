
nums = [7 ,12 ,9 ,8 ,9 ,15]
k = 4
result = 0
for bit in range(31, -1, -1):
    count = 0

    # Count the number of elements in nums with the bit set at the current position
    for num in nums:
        if num & (1 << bit):
            count += 1

    # If the count of elements with the bit set is at least k, set that bit in the result
    if count >= k:
        result |= (1 << bit)
print(result)
