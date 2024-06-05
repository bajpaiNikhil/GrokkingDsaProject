import heapq

s = "Programming"
freqHashMap = {}
minHeap = []

for i in s:
    freqHashMap[i] = freqHashMap.get(i, 0) + 1
print(freqHashMap)

for key, val in freqHashMap.items():
    heapq.heappush(minHeap, (-val, key))
print(minHeap)
res = ""
while minHeap:
    poppedItem = heapq.heappop(minHeap)
    res += poppedItem[1]* -poppedItem[0]
print(res)

# dic = {}
# for i in s:
#     if i not in dic:
#         dic[i] = 0
#     dic[i ] +=1
# print(dic)
# heap =[]
# for key,val in dic.items():
#     heap.append((-val,key))
# print(heap)
# heapq.heapify(heap)
# print(heap)
# ans = ""
#
# for i in range(len(dic)):
#     print(i)
#     k = heapq.heappop(heap)
#     ans+= k[1]*(-k[0])
# print(ans)
