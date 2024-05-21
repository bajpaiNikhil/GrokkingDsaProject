grid = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
rows = len(grid)
columns = len(grid[0])

for row in range(rows):
    print(row)
    if grid[row][0] == 0:
        for col in range(columns):
            grid[row][col] = 0 if grid[row][col] else 1
# print(grid)

for c in range(columns):
    one_count = 0
    for r in range(rows):
        one_count += grid[r][c]
    if one_count < rows - one_count:
        for r in range(rows):
            grid[r][c] = 0 if grid[r][c] else 1
# print(grid)
gridSum = 0
for i in grid:
    # print("".join(map(str, i)))
    gridSum+=int("".join(map(str, i)),2)
print(gridSum)