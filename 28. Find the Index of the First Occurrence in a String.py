haystack = "mississippi"
needle = "issip"
# "mississippi"
# "issip"
hLength = len(haystack)
nLength = len(needle)

nIndex = 0
i=0
while i < hLength:
    if haystack[i] == needle[nIndex]:
        nIndex += 1
        i += 1
    else:
        # Reset `i` to account for mismatched characters
        i = i - nIndex + 1
        nIndex = 0

    if nIndex == nLength:
        print(i - nIndex)
        exit()
print(-1)
exit()