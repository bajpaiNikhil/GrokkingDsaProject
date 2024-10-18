s = "0P"
t = "".join(c.lower() for c in s if c.isalnum())
print(t)
left = 0
right = len(t)-1

while left< right:
    if t[left] != t[right]:
        print(False)
        exit()
    left+=1
    right-=1
print(True)
exit()
