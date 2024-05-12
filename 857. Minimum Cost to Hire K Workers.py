import heapq

quality = [10, 20, 5]
wage = [70, 50, 30]
k = 2
heap = []
for i in range(len(quality)):
    heap.append(((wage[i] / quality[i]), quality[i]))
heap.sort()
heapIs = []
qualitySum = 0
ret = float('inf')
# heapq.heapify(heap)
# print(heap)
for ratio, q in heap:
    # print(ratio, q)
    heapq.heappush(heapIs, -q)
    qualitySum += q
    print(ratio,q,qualitySum,heapIs)
    if len(heapIs) > k: qualitySum += heapq.heappop(heapIs)
    if len(heapIs) == k: ret = min(ret, qualitySum * ratio)
print(ret)
