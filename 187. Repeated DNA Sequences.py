

from  collections import  defaultdict

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
d = defaultdict(int)
ans = []
for i in range(len(s)):
    dna = s[i:i+10]
    d[dna] +=1
    if d[dna]== 2:
        ans.append(s[i:i+10])
print(ans)