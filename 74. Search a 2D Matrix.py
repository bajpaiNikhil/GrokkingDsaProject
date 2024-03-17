matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 344

for i in matrix:
    # insert binary search
    left = 0
    right = len(i)-1

    while left<= right:
        mid = left+(right-left)//2
        if i[mid] == target:
            print(True)
            break
        elif i[mid]>target:
            right = mid-1
        else:
            left = mid+1
print(False)
