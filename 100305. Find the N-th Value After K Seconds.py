n = 4
k = 5
MOD = 10 ** 9 + 7

dp = [[0] * n for _ in range(k + 1)]
print(dp)
for j in range(n):
    dp[0][j] = 1

for i in range(1, k + 1):
    prefix = [0] * n
    prefix[0] = dp[i - 1][0]
    for j in range(1, n):
        prefix[j] = (prefix[j - 1] + dp[i - 1][j]) % MOD

    for j in range(n):
        dp[i][j] = prefix[j]

print(dp)
print(dp[k][n - 1])
