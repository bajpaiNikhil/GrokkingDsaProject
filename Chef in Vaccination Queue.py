

n = int(input())
for _ in range(n):
    n,p,x,y = map(int,input().split())
    queueIs = list(map(int,input().split()))
    print(n,p,x,y)
    print(queueIs)
    waitTime = 0
    for person in range(1,int(n)+1):
        if queueIs[person-1] == 0:
            waitTime+= int(x)
        elif queueIs[person-1] == 1 and person == p:
            waitTime+=int(y)
            break
        else:
            waitTime+=int(y)
    print(waitTime)

