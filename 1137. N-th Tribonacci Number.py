def tribonacci(n):
    dp = {0: 0, 1: 1, 2: 1}

    def helper(a):
        if a in dp:
            return dp[a]
        dp[a] = helper(a - 1) + helper(a - 2) + helper(a - 3)
        return dp[a]

    return helper(n)

    # dp = {}
    #
    # def helper(a, dp):
    #     if a == 0:
    #         return a
    #     if a == 1:
    #         return 1
    #     if a == 2:
    #         return 1
    #     else:
    #         if a not in dp:
    #             dp[a] = helper(a - 1, dp) + helper(a - 2, dp) + helper(a - 3, dp)
    #         return dp[a]

    # return helper(n, dp)


n = 25
print(tribonacci(n))
