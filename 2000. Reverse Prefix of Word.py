word = "rzwuktxcjfpamlonbgyieqdvhs"
ch = "s"

pointerToReverse = 0
for i in range(len(word)):
    if word[i] == ch:
        pointerToReverse = i
        break
k  =  word[0:pointerToReverse+1]
print(pointerToReverse , k ,k[::-1]+word[pointerToReverse+1:])