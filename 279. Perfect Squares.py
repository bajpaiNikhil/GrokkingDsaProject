import math
from math import sqrt


def perfectSquare(n):

    def helper(n,memo):
        if n == 0:
            return 0
        if n in memo:
            return memo[n]
        minSquare = math.inf
        for i in range(1,int(sqrt(n))+1):
            square = i*i
            numsSquare = 1+helper(n-square,memo)
            minSquare= min(minSquare,numsSquare)
        memo[n] = minSquare
        return minSquare

    return helper(n,{})


n = 13
print(perfectSquare(n))