import math

n = 100000
quantities = [4,4,4,2,4,2,4,1,5,4,5,4,1,1,2,2,4,1,1,4,5,3,3,4,1,2]

def check(quantities, mid, n):
    return sum(math.ceil(pile / mid) for pile in quantities) <= n


left = 0
right = max(quantities)
ans = 0
while left <= right:
    mid = left + (right - left) // 2

    if mid!=0 and check(quantities, mid, n) :
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)
