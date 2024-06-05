import heapq

nums = [1,1,1,2,2,3]

k = 2
freqHash = {}
minHeap = []
for i in nums:
    freqHash[i] = freqHash.get(i,0)+1
print(freqHash)
for key, val in freqHash.items():
    heapq.heappush(minHeap,(val,key))
    if len(minHeap) > k:
        heapq.heappop(minHeap)

res = []
while minHeap:
    res.append(heapq.heappop(minHeap)[1])
print(res)


# dic = {}
# for i in nums:
#     if i not in dic:
#         dic[i] = 0
#     dic[i]+=1
# print(dic)
# unique_nums = list(dic.keys())
# print(unique_nums)
# heap = [(dic[i],i) for i in unique_nums[:k] ]
# print(heap)
# heapq.heapify(heap)
# print(heap)
# for i in unique_nums[k:]:
#     heapq.heappushpop(heap ,(dic[i],i))
# print(heap)
# print([i[1] for i in heap])
