import heapq

nums = [4, 1, 5, 20, 3]
heap = [-num * 2 if num % 2 != 0 else -num for num in nums]
# print(heap)
heapq.heapify(heap)
# print(heap)
minVal = float('inf')
# print(minVal)
for num in nums:
    minVal = min(minVal, num if num % 2 == 0 else num * 2)
# print(minVal)
minDeviation = float('inf')
while True:
    maxElementValue = -heapq.heappop(heap)
    minDeviation = min(minDeviation, maxElementValue - minVal)
    if maxElementValue % 2 != 0:
        break
    maxElementValue //= 2
    minVal = min(minVal, maxElementValue)
    heapq.heappush(heap, -maxElementValue)
print(minDeviation)
