bloomDay = [7,7,7,7,12,7,7]
m = 2
k = 3


def check(arr, mid, m):
    bonquets, flowers = 0, 0
    for i in arr:
        if i > mid:
            flowers = 0
        else:
            bonquets += (flowers + 1) // k
            flowers = (flowers + 1) % k
    return bonquets >= m


left = 1
right = max(bloomDay)
ans = 0

if len(bloomDay) < m * k:
    print(-1)

while left <= right:
    mid = left + (right - left) // 2
    if check(bloomDay, mid, m):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans if ans != 0 else -1)
