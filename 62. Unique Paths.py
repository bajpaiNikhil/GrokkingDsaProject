def countPath(r, c, m, n, memo):

    post = str(r) + ", " + str(c)
    if r == m or c == n:
        return 0
    if r == m - 1 and c == n - 1:
        return 1
    if post in memo:
        return memo[post]

    downCount = countPath(r + 1, c, m, n, memo)
    rightCount = countPath(r, c + 1, m, n, memo)
    memo[post] = downCount + rightCount
    return downCount + rightCount


m = 3
n = 7
print(countPath(0,0,m,n,{}))