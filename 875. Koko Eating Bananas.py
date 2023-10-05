import math

piles = [30, 11, 23, 4, 20]
h = 6
left = 1
right = max(piles)
ans = 0


def check(arr, mid, h):
    return sum(math.ceil(pile / mid) for pile in arr) <= h


while left <= right:
    mid = left + (right - left) // 2
    if check(piles, mid, h):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)
