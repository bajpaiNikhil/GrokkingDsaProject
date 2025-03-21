t = int(input())
for t in range(t):
    n = int(input())
    books = list(map(int,input().split()))
    dic= {}
    for i in range(len(books)):
        dic[books[i]] = i
    print(dic)
    penalty = 0
    for key,val in dic.items():
        penalty+=val+1
    print(penalty)

