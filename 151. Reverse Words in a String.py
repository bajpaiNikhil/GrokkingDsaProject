def reverseTheWord(s, start, end):
    left = start
    right = end - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s


def reverseTheSentence(s):
    s = list(s[::-1])
    start = 0
    end = 0
    while start < len(s):
        # print("start", start, end)
        while end < len(s) and s[end] != " ":
            print("end", start, end)
            end += 1
        print("doSomething", start, end)
        # print("here",start , end,k )

        k = reverseTheWord(s, start, end)
        print("here", start, end, k, s)

        start = end + 1
        end += 1
        # print("here",start , end,k )
    return "".join(s)


s = "the sky is blue"
print(reverseTheSentence(s))
