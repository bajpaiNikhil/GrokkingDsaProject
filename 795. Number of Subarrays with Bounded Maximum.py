



nums = [2,1,4,3]
left = 2
right = 3

ans = mid = low =0
for num in nums :

    if num > right : mid = 0
    else :
        mid +=1
        ans += mid
    if num >= left : low = 0
    else :
        low +=1
        ans -= low
print(ans)

