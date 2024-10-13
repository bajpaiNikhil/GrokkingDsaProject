t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    nums = list(map(int, input().split()))
    a = all(x == 1 for x in nums)
    b = all(x == 1 for x in nums[:m])
    if a:
        print(100)
    elif not a and b:
        print(50)
    else:
        print(0)
