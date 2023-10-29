
s = "1001"
ans = 0
for i in range(0,len(s)-1,2):
    if s[i]!=s[i+1]:
        ans+=1
print(ans)