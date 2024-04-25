import heapq

words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4

dic = {}
for word in words:
    if word not in dic:
        dic[word] = 0
    dic[word] += 1
print(dic)
heap = []
# The negative sign is used to make sure that higher frequencies are treated as lower values,
# thus allowing the heap to maintain the maximum frequencies at the top.
# Then, we use heapq.heapify() to transform the list into a heap data structure.
for key,val in dic.items():
    heap.append((-val,key))
print(heap)
heapq.heapify(heap)
print(heap)
t = []
for i in range(k):
    t.append(heapq.heappop(heap)[1])
    print(heap)
print(t)