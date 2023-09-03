a = [["#", "#", "*", ".", "*", "."],
     ["#", "#", "#", "*", ".", "."],
     ["#", "#", "#", ".", "#", "."]]
n = len(a)
m = len(a[0])
res = [["."] * n for k in range(m) ]
print(res)
for i in range(n):
    base = m - 1
    for j in range(m-1, -1, -1):
        if a[i][j] == "#":
            res[base][n-i-1] = "#"
            base-=1
        elif  a[i][j] == "*" :
            res[j][n-i-1]= "*"
            base = j -1
print(res)
