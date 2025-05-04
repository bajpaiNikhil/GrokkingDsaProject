x = 121

x = str(x)

left = 0
right = len(x)-1

while left< right:
    if x[left]!= x[right]:
        print(False)
        exit()
    left+=1
    right-=1
print(True)