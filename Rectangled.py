n = int(input())
for _ in range(n):
    inkUnit = int(input())
    if inkUnit <=1 :
        print(0)
    else:
        length  = inkUnit//4
        width = inkUnit//2 - length
        area = length*width
        print(area)

