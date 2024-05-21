grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]

maxGold = 0


def dfs(i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
        return 0
    currentGold = grid[i][j]
    grid[i][j] = 0
    maxGold = max(dfs(i - 1, j), dfs(i + 1, j), dfs(i, j + 1), dfs(i, j - 1))
    grid[i][j] = currentGold
    return currentGold + maxGold


for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != 0:
            maxGold = max(maxGold, dfs(i, j))
print(maxGold)