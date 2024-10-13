
def construct_matrix(N, M):
    for i in range(N):
        row = []
        for j in range(M):
            row.append(i + j + 2)  # Start from 2 to ensure the constraint 2 <= A[i][j]
        print(" ".join(map(str, row)))


N = 2  # Number of rows
M = 3  # Number of columns
construct_matrix(N, M)