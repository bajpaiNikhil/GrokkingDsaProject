
s = "axc"
t = "ahbgdc"

if len(s) > len(t): print(False)
if len(s) == 0: print(True)
subsequence = 0
for i in range(0, len(t)):
    if subsequence <= len(s) - 1:
        # print(s[subsequence])
        if s[subsequence] == t[i]:
            subsequence += 1
print(subsequence == len(s))
