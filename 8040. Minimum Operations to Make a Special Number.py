from functools import cache

num_str = "2908305"
min_operations = float('inf')

for i in range(len(num_str) - 2):
    for j in range(i + 1, len(num_str) - 1):
        candidate = num_str[i] + num_str[j]
        remaining_digits = num_str[:i] + num_str[j + 1:]

        # Check if candidate forms a special number (divisible by 25)
        if candidate in ["00", "25", "50", "75"]:
            # Calculate the number of operations required
            operations = len(remaining_digits) + 2  # Two digits chosen
            min_operations = min(min_operations, operations)

print(min_operations if min_operations != float('inf') else 0)