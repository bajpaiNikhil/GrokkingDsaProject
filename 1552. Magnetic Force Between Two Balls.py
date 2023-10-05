
position = [5,4,3,2,1,1000000000]
m = 2

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

position.sort()
left = 1
right = max(position)
ans = 0
while left <= right :
    mid = left + (right -left) // 2
    if check(position, mid, m):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1
print(ans%10**9)
