import heapq

s = "aaab"
freqHashMap = {}
maxHeap = []
for i in s:
    freqHashMap[i] = freqHashMap.get(i,0)+1
print(freqHashMap)

for key,val in freqHashMap.items():
    heapq.heappush(maxHeap,(-val,key))

previousChar = None
previousFrequency = 0
print(freqHashMap,maxHeap)
res = ""
while maxHeap:
    val , key = heapq.heappop(maxHeap)

    if key and -previousFrequency>0:
        heapq.heappush(maxHeap,(previousFrequency,previousChar))
    res+=key
    previousChar = key
    previousFrequency = val+1
print(res)
# heap = []
# dic = {}
# for i in s:
#     dic[i] = dic.get(i, 0) + 1
#
# print(dic)
# for key, val in dic.items():
#     heap.append((-val, key))
# print(heap)
# heapq.heapify(heap)
# print(heap)
# res = []
# while len(heap) >= 2:
#     freq1, char1 = heapq.heappop(heap)
#     freq2, char2  = heapq.heappop(heap)
#     res.extend([char1,char2])
#     if freq1+1 < 0 :
#         heapq.heappush(heap,(freq1+1,char1))
#     if freq2+1 < 0:
#         heapq.heappush(heap,(freq2+1,char2))
# print("heap and res ", heap,res)
#
# if heap:
#     freq ,char = heapq.heappop(heap)
#     print(char,freq,heap)
#     if -freq > 1:
#         print("")
#     res.append(char)
# print("".join(res))
