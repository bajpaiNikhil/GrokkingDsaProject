import math

piles = [30,11,23,4,20]
h = 5
# left = 1
# right = max(piles)
# ans = 0
#
#
# def check(arr, mid, h):
#     return sum(math.ceil(pile / mid) for pile in arr) <= h
#
#
# while left <= right:
#     mid = left + (right - left) // 2
#     if check(piles, mid, h):
#         ans = mid
#         right = mid - 1
#     else:
#         left = mid + 1
# print(ans)


def check(mid, piles, h):
    timeSpent = 0
    for i in piles:
        timeSpent += math.ceil(i / mid)
        if timeSpent > h:
            return False
    return True


left = 1
right = max(piles)
ans = 0
while left <= right:
    mid = left + (right - left) // 2

    if check(mid, piles, h):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)
