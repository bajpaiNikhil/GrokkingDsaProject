

t = int(input())
for t in range(t):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    n = int(input())
    a = input()
    b = input()
    c = input()
    d = ""
    k = (alphabets.index(b[0])*25)-alphabets.index(a[0])
    print(k)
    for i in c:
        d+= alphabets[(alphabets.index(i) + k)%25]
    print(d)
