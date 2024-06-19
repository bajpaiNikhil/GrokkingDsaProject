


def findOnesCount(k):
    ans = 0
    while k:
        k &= (k - 1)
        ans += 1
    return ans


n = 5
l = list(range(n))
# print(l)
for i in range(len(l)):
    l[i] = findOnesCount(l[i])

print(l)