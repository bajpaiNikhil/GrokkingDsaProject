num = 430043
k = 2
count = 0
for windowEnd in range(len(str(num)) - k + 1):
    # print(windowEnd , str(num)[windowEnd])
    divisorIs = int(str(num)[windowEnd:windowEnd+k])
    # print(divisorIs)
    if divisorIs and num%divisorIs==0:
        count+=1
print(count)


# print(windowEnd , str(num)[windowEnd])
