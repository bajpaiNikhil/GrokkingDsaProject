rolls = [1, 5, 6]
mean = 3
n = 4
m = len(rolls)
missingSum = mean * (n + m) - sum(rolls)
# print(missingSum)
part = missingSum // n
rem = missingSum % n
# print(part, rem)
ans = []
for i in range(n):
    print(i, i < rem, part)
    if i < rem:
        ans.append(part + 1)
        # print(ans)
    else:
        ans.append(part)
        # print(ans)
print(ans)
