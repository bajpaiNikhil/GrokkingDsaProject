words = ["abc","car","ada","racecar","cool"]

def isPalindrome(item):
    left = 0
    right = len(item)-1
    while left<= right:
        if item[left] == item[right]:
            left+=1
            right-=1
        else:
            return False
    return True

for i in words:
    if isPalindrome(i):
        print(i)
        exit(0)
