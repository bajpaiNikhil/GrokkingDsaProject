



s = [3,2,5,1,3,4]
s.sort()
left = 0
right = len(s)-1
target = s[left]+ s[right]
productIs = 0
while left < right :
    if s[left]+s[right] != target:
        print(-1)
        break
    else:
        productIs+=(s[left]*s[right])
        left+=1
        right-=1

print(productIs)