x = 23

l = []
a = x
while x:
    l.append(x % 10)
    x = x // 10
print(l)
print(sum(l),a)
print(a % sum(l))
