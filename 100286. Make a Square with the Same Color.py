matrix = [["B", "B", "B"], ["B", "B", "B"], ["B", "B", "B"]]
submatrices = []

for i in range(len(matrix) - 1):
    for j in range(len(matrix[0]) - 1):
        # Extract the 2x2 submatrix
        # submatrix = [
        #     [matrix[i][j], matrix[i][j + 1]],
        #     [matrix[i + 1][j], matrix[i + 1][j + 1]]
        # ]
        l = [matrix[i][j], matrix[i][j + 1], matrix[i + 1][j], matrix[i + 1][j + 1]]
        if (l.count("B") == 3 and l.count("W")) == 1 or (l.count("W") == 3 and l.count("B")) or l.count("B") == 4 or l.count("W") == 4:
            print(True, l)
            break
        # print(submatrix,matrix[i][j], matrix[i][j + 1],matrix[i + 1][j], matrix[i + 1][j + 1])
        # submatrices.append(submatrix)
print(False)
