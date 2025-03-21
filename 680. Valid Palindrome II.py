s = "abcwfwea"


def isPalindrome(s, left, right):
    while left <= right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

left = 0
right = len(s)-1
while left <= right:
    if s[left]== s[right]:
        left+=1
        right-=1
    else:
        print(isPalindrome(s,left,right-1) or isPalindrome(s,left+1,right))
        exit()
print(True)
exit()
