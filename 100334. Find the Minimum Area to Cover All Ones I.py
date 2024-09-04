

grid = [[0,1]]
minRow,maxRow = len(grid),-1
minCol,maxCol = len(grid[0]),-1
found_one = False
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == 1:
            found_one = True
            minRow = min(row,minRow)
            maxRow = max(row,maxRow)
            minCol = min(col,minCol)
            maxCol = max(col,maxCol)
if not found_one:
    print(0)
    exit(0)
height = maxRow-minRow +1
weidth = maxCol-minCol +1
print(height*weidth)

