import heapq
import math

arr = [1, -2, 3, 89, 900, 100, 0]
# first iteration would be  max1 = 1 and max2 = 0
# second iteration would max1 = 2 and max2 =1
# third iteration would max1 =
max1 = -math.inf
max2 = -math.inf
for i in range(len(arr)):
    if arr[i] > max1:
        max2 = max1
        max1 = arr[i]
        # max2 = max1
    elif max2 < arr[i] < max1:
        max2 = arr[i]
print(max1, max2)
maxheap = []
for i in arr:
    heapq.heappush(maxheap,-i)
print(maxheap)