from math import sqrt

nums = [2, 2]

windowStart = 0
windowSize = 0
maxSize = 0


def isPrime(n):
    # Corner case
    if n <= 1:
        return False

    # Check from 2 to sqrt(n)
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


primeIndex = [i for i, num in enumerate(nums) if isPrime(num)]
print(primeIndex)
maxDiff = 0
left , right = 0,0
l = []
for i in range(len(nums)):
    if isPrime(nums[i]):
        l.append(i)
print(l)
if len(l)>1:
    print(abs(min(l) - max(l)))
