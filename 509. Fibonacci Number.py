def fib(a):
    dp = {}

    def helper(a, dp):
        if a <= 1:
            return a
        else:
            if a not in dp:
                dp[a] = helper(a - 1, dp) + helper(a - 2, dp)
            return dp[a]

    return helper(a, dp)


n = 568
print(fib(n))
