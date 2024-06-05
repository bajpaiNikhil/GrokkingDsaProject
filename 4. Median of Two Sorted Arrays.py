import heapq
from math import ceil

nums1 = [1,2]
nums2 = [3,4]
minHeap = []

if len(nums1)>0:
    heapq.heappush(minHeap,(nums1[0],0,nums1))
if len(nums2)> 0:
    heapq.heappush(minHeap,(nums2[0],0,nums2))
print(minHeap)
n = len(nums1)+len(nums2)
k = n//2 if n%2 == 0 else ceil(n/2)
count = 0
result = 0
while minHeap:
    number , index , listIs = heapq.heappop(minHeap)

    count +=1
    if n%2 ==0:
        if count == k or count == k+1:
            result+=number
    else:
        if count == k:
            result+=number
    if index+1 < len(listIs):
        heapq.heappush(minHeap,(listIs[index+1],index+1,listIs))
print(result if n%2 == 1 else result/2)