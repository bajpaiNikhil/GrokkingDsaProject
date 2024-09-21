
def backTrackFunc(n, leftCount, rightCount, result, output):
    if leftCount>= n and rightCount>=n:
        output.append("".join(result))
    if leftCount<n:
        result.append("(")
        backTrackFunc(n,leftCount+1,rightCount,result,output)
        result.pop()
    if rightCount<leftCount:
        result.append(")")
        backTrackFunc(n,leftCount,rightCount+1,result,output)
        result.pop()

n = 3
result = []
output =[]
backTrackFunc(n,0,0,result,output)
print(output)