

grid = [[1,0,2],[1,0,2]]

for row in range(len(grid)):
    for colm in range(len(grid[0])):
        # print(grid[row][colm],row,colm , grid[row+1][colm],grid[row][colm+1])
        # grid[i][j] == grid[i + 1][j] or (j < n - 1 and grid[i][j] == grid[i][j + 1])
        if len(grid) != row+1 and grid[row][colm] != grid[row + 1][colm]:
            print(False)
        if len(grid[0])!= colm+1 and grid[row][colm] == grid[row][colm + 1]:
            print(False)
            # break
    # break
print(True)
