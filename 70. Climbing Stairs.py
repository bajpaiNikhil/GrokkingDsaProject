

n = 44

def climbingStart(n):
    dp = {}

    def helper(a,dic):
        if a == 1:
            return 1
        if a == 2:
            return 2
        if a in dic:
            return dic[a]
        else:
            dic[a]  = helper(a-1,dic) +helper(a-2,dic)
            return dic[a]
    return helper(n,dp)
print(climbingStart(n))
