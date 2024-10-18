bills = [5, 10, 20]

fiveCount = 0
tenCount = 0
twentyCount = 0
for i in bills:
    if i == 5:
        fiveCount += 1
    elif i == 10:
        if fiveCount == 0:
            print(False)
            exit()
        fiveCount -= 1
        tenCount += 1
    else: # bill 20
        if tenCount>0 and fiveCount >0:
            tenCount-=1
            fiveCount-=1
        elif fiveCount>=3:
            fiveCount-=3
        else:
            print(False)
            exit()

print(True)
exit()
