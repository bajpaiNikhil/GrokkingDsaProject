# def findKnapsack(w, v, c, n):
#     if n == 0 or c == 0:
#         return 0
#     if w[n - 1] > capacity:
#         return findKnapsack(w, v, c, n - 1)
#     else:
#         return max(value[n - 1] + findKnapsack(v, w, c - w[n - 1], n - 1), findKnapsack(v, w, c, n - 1))

def find_knapsack(capacity, weights, values, n):
    # create a table to store the maximum value at each n and capacity
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


weight = [1, 2, 3, 5]
value = [10, 5, 4, 8]
capacity = 5
print(find_knapsack(capacity,weight, value, len(weight)))
