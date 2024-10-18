def rearrange_maximize_odd_prefix(arr):
    # Separate odd and even numbers
    odd_numbers = [x for x in arr if x % 2 != 0]
    even_numbers = [x for x in arr if x % 2 == 0]

    result = []

    # Define the alternating pattern (start with odd)
    i, j = 0, 0
    while i < len(odd_numbers) and j < len(even_numbers):
        result.append(odd_numbers[i])
        i += 1
        if j < len(even_numbers):
            result.append(even_numbers[j])
            j += 1
        if j < len(even_numbers):
            result.append(even_numbers[j])
            j += 1
        if i < len(odd_numbers):
            result.append(odd_numbers[i])
            i += 1
    while i < len(odd_numbers):
        result.append(odd_numbers[i])
        i += 1
    while j < len(even_numbers):
        result.append(even_numbers[j])
        j += 1

    return result


# def calculate_prefix_sum(arr):
#     prefix_sum = []
#     current_sum = 0
#     for num in arr:
#         current_sum += num
#         prefix_sum.append(current_sum)
#     return prefix_sum


# Example usage
arr = [4,4,4]
rearranged_array = rearrange_maximize_odd_prefix(arr)

prefix_sum = []
current_sum = 0
for num in rearranged_array:
    current_sum += num
    prefix_sum.append(current_sum)
print(prefix_sum)
# prefix_sum_array = calculate_prefix_sum(rearranged_array)

print("Original Array:", arr)
print("Rearranged Array:", rearranged_array)
# print("Prefix Sum Array:", prefix_sum_array)

