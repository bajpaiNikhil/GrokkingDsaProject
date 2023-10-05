
grades = [10 ,6 ,12 ,7 ,3 ,5]
left = 0
right = 1000
n= len(grades)
while left < right:
    mid = (left + right + 1) // 2

    if mid * (mid + 1) // 2 <= n:
        left = mid
    else:
        right = mid - 1
print(left)
