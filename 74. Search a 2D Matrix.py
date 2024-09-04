matrix = [[1,3]]
target = 3

for i in matrix:
    # insert binary search
    left = 0
    right = len(i)-1

    while left<= right:
        mid = left+(right-left)//2
        print(mid,left,right ,i[mid])
        if i[mid] == target:
            print(True)
            break
        elif i[mid]>target:
            right = mid-1
        else:
            left = mid+1
print(False)
print(9//3)
print(9% 3)