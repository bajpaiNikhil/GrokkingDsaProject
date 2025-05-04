import math
from math import sqrt


# def perfectSquare(n):
#
#     def helper(n,memo):
#         if n == 0:
#             return 0
#         if n in memo:
#             return memo[n]
#         minSquare = math.inf
#         for i in range(1,int(sqrt(n))+1):
#             square = i*i
#             numsSquare = 1+helper(n-square,memo)
#             minSquare= min(minSquare,numsSquare)
#         memo[n] = minSquare
#         return minSquare
#
#     return helper(n,{})


def perfectSquare(n):
    dp = {}
    def helper(a,dic):
        if a == 0:
            return 0
        if a in dic:
            return dic[a]
        ans = math.inf
        for i in range(1,int(sqrt(a))+1):
            square = i*i
            ans = min(ans , helper(a-square,dic)+1)
        dic[a] = ans
        return dic[a]
    return helper(n,dp)
n = 12
print(perfectSquare(n))