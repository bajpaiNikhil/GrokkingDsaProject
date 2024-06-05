import heapq
import math

nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
currentMaxNumber = -math.inf
rangeStart , rangeEnd = 0,math.inf
minHeap =[]

for list in nums:
    heapq.heappush(minHeap,(list[0],0,list))
    currentMaxNumber = max(currentMaxNumber,list[0])
print(minHeap,currentMaxNumber)

while len(minHeap) == len(nums):
    number ,index, listIs = heapq.heappop(minHeap)

    if rangeEnd-rangeStart > currentMaxNumber-number:
        rangeStart = number
        rangeEnd = currentMaxNumber
    if len(listIs)>index+1:
        heapq.heappush(minHeap,(listIs[index+1],index+1,listIs))
        currentMaxNumber = max(currentMaxNumber,listIs[index+1])
print([rangeStart ,rangeEnd])