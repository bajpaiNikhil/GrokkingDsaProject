s1 = "abcdba"
s2 = "cabdab"


# "bnxw"
# "bwxn"
s1=list(s1)
s2 = list(s2)
count=1
for i  in range(0,len(s1)-2):
    a = s1[i]+s1[i+2]
    b = s2[i]+s2[i+2]
    print(a,b)
    if sorted(a)!= sorted(b):
        print(False)
        break
print(True)