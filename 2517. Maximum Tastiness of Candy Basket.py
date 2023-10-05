prices = [13, 5, 1, 8, 21, 2]
k = 3


def check(prices, mid, k):
    lastPlaced = prices[0]
    count = 1

    for i in range(len(prices)):
        if prices[i] - lastPlaced >= mid:
            count += 1
            lastPlaced = prices[i]
            if count == k:
                return True
    return False


left = 0
right = max(prices)
ans = 0
prices.sort()
while left <= right:
    mid = left + (right - left) // 2
    if check(prices, mid, k):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1
print(ans)
