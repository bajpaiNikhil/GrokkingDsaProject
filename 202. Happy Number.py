n = 23

slow = n
fast = n


def findSquare(num):
    _sum = 0
    while num > 0:
        digit = num % 10
        _sum += digit * digit
        num //= 10
    return _sum


while True:
    slow = findSquare(slow)
    fast = findSquare(findSquare(fast))
    print(slow, fast)
    if slow == fast:
        break
    else:
        continue
print(slow == 1)
