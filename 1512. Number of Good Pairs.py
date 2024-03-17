nums = [1, 2, 3, 1, 1, 3]

d = {}
for i in nums:
    if i not in d:
        d[i]=0
    d[i]+=1
ans = 0
for i in d.values():
    ans+=(i*(i-1)//2)
print(ans)