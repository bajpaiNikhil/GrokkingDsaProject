# def findKnapsack(w, v, c, n):
#     if n == 0 or c == 0:
#         return 0
#     if w[n - 1] > capacity:
#         return findKnapsack(w, v, c, n - 1)
#     else:
#         return max(value[n - 1] + findKnapsack(v, w, c - w[n - 1], n - 1), findKnapsack(v, w, c, n - 1))

# def find_knapsack(capacity, weights, values, n):
#     # create a table to store the maximum value at each n and capacity
#     dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
#
#     # Build table dp[][] in bottom-up manner
#     for i in range(n + 1):
#         for w in range(capacity + 1):
#             if i == 0 or w == 0:
#                 dp[i][w] = 0
#             elif weights[i - 1] <= w:
#                 dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
#             else:
#                 dp[i][w] = dp[i - 1][w]
#
#     return dp[n][capacity]

def find_knapsack(c, w, v, n,dp):
    if n == 0 or c ==0 :
        return 0
#     create a key for the current state
    key = (n,c)
#     if result is already computed
    if key in dp:
        return dp[key]
#     choice : include or exclude.
    if w[n-1]<= capacity:
        include = v[n-1]+find_knapsack(c-w[n-1],w,v,n-1,dp)
        exclude = find_knapsack(c,w,v,n-1,dp)
        dp[key] =  max(include,exclude)
    else:
        dp[key] = find_knapsack(c,w,v,n-1,dp)
    return dp[key]



weight = [1, 2, 3, 5]
value = [5, 4, 8, 6]
capacity = 5
print(find_knapsack(capacity,weight, value, len(weight),{}))
