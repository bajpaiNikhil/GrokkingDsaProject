s = "abada"
c = "a"
count = 0
n = len(s)

# Initialize an array to store the count of 'c' from each index to the end
count_c = [0] * n
total_c = 0

# Calculate the count of 'c' from right to left
for i in range(n - 1, -1, -1):
    if s[i] == c:
        total_c += 1
    count_c[i] = total_c
print(count_c)
# Iterate through the string
for i in range(n):
    if s[i] == c:
        # For each occurrence of 'c', add the count of 'c' after this position
        count += count_c[i]

print(count)
