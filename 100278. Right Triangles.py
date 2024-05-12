grid = [[1,0,0,0],[0,1,0,1],[1,0,0,0]]
row_count = {}
col_count = {}
count = 0
# Iterate through the matrix
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 1:
            row_count[i] = row_count.get(i, 0) + 1
            col_count[j] = col_count.get(j, 0) + 1

# Calculate the total count
count = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 1:
            count += (row_count[i] - 1) * (col_count[j] - 1)
# for i, j in enumerate(grid):
#     rowSum[i] = sum(j)
# print(rowSum)
#
# for row in grid:
#     for j, value in enumerate(row):
#         columnSum[j] += value
# print(columnSum)
# count = 0
# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         # print(grid[i][j])
#         if grid[i][j] == 1:
#             count += (rowSum[i] - 1) * (columnSum[j] - 1)
print(count)
