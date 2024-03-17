nums = [2,5,1,3,4,7]
n = 3

ans = []
for i,j in zip(nums[:n],nums[n:]):
    # print(i,j)
    ans += [i,j]
print(ans)