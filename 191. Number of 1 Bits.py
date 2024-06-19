n = 2147483645
count  = 0
while n > 0:
    binary = n % 2
    # print(binary)
    if binary == 1:
        count += 1
    n = n // 2
print(count)