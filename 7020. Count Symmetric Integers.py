


low = 100
high = 120
count=0
for i in range(low,high+1):
    a = list(map(int, str(i)))
    if len(a) %2 ==0 and sum(a[:len(a)//2]) == sum(a[len(a)//2:]):
        print(a,a[:len(a)//2],a[len(a)//2:])
        count+=1
print(count)