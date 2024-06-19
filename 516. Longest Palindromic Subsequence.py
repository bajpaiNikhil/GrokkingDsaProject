def longestPalindromeSubSeq(s, start, end, memo):
    key = f"{start},{end}"
    if key in memo:
        return memo[key]
    if len(s) == 0:
        return 1
    if start>end :
        return  0
    if s[start] == s[end]:
        memo[key] =  2+ longestPalindromeSubSeq(s,start+1,end-1,memo)
    else:
        memo[key] =  max(longestPalindromeSubSeq(s,start+1,end,memo),longestPalindromeSubSeq(s,start,end-1,memo))
    return memo[key]

s = "cbbd"
print(longestPalindromeSubSeq(s , 0,len(s)-1,{}))