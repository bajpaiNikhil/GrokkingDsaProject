s = "baeyh"
k = 2
count = 0
vowel = {'a','e','i','o','u'}
for i in range(len(s)):
    c , v =0 , 0
    for j in range(i,len(s)):
        print(s[j])
        if s[j] in vowel:
            v+=1
        else:
            c+=1
        if c == v and (v*c)%k == 0:
            count+=1
print(count)