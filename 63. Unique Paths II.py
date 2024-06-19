

def uniquePathsWithObstacles(obstacleGrid) -> int:
    def helper(g, r, c, memo):
        post = str(r) + "," + str(c)
        if r == len(g) or c == len(g[0]) or g[r][c] == 1:
            return 0
        if r == len(g) - 1 and c == len(g[0]) - 1:
            return 1
        if post in memo:
            return memo[post]

        downCount = helper(g, r + 1, c, memo)
        rightCount = helper(g, r, c + 1, memo)
        # print(downCount + rightCount)
        memo[post] = downCount + rightCount
        return downCount + rightCount

    return helper(obstacleGrid, 0, 0, {})

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(uniquePathsWithObstacles(obstacleGrid))