
n = 2
m = 3
hBars = [2,3]
vBars = [2,3,4]
hBars.sort()
vBars.sort()
countHbar = 1
consecutiveHbar = 1
consecutiveVbar = 1
countVbar = 1
for i in range(1,len(hBars)):
    # print(hBars[i],hBars[i-1]+1,consecutiveHbar,countHbar)
    if hBars[i] == hBars[i-1]+1:
        #print(hBars[i], hBars[i - 1] + 1, consecutiveHbar, countHbar)
        countHbar+=1
    else:
        countHbar = 1
    consecutiveHbar = max(countHbar , consecutiveHbar)
# print(consecutiveHbar)
for j in range(1,len(vBars)):
    if vBars[j] == vBars[j-1]+1:
        countVbar+=1
    else:
        countVbar = 1
    consecutiveVbar = max(consecutiveVbar,countVbar)
# print(consecutiveVbar)
squareSide = min(consecutiveVbar+1 , consecutiveHbar+1)
# print(squareSide)
print(squareSide*squareSide)
