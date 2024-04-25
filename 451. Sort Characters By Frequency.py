import heapq

s = "abaccadeeefaafcc"
dic = {}
for i in s:
    if i not in dic:
        dic[i] = 0
    dic[i ] +=1
print(dic)
heap =[]
for key,val in dic.items():
    heap.append((-val,key))
print(heap)
heapq.heapify(heap)
print(heap)
ans = ""

for i in range(len(dic)):
    print(i)
    k = heapq.heappop(heap)
    ans+= k[1]*(-k[0])
print(ans)
