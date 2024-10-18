
for t in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    susWealth = l[-1]
    currentPosition = len(l)
    # print(currentPosition)
    for i in range(len(l) - 2, -1, -1):
        # print(l[i])
        if (susWealth // 2) >= l[i]:
            currentPosition -= 1
            # print(currentPosition, l[i], susWealth)
        else:
            break
    print(currentPosition)

