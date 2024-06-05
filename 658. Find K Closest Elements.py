import heapq


def binarySearchForIndexOfX(arr,target):
    left  = 0
    right = len(arr)-1
    ans = 0
    while left<=right:
        mid = left+(right-left)//2
        # print(left,right)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            ans = mid # Update ans to mid if target is greater than arr[mid]
            left = mid+1 # Move left bound up
        else:
            right = mid-1 # Move right bound down
    return ans

arr = [1]
k = 1
x = 1
index = binarySearchForIndexOfX(arr,x)
print(index)
leftRange = max(index - k,0)
rightRange = min(index + k,len(arr)-1)
print(leftRange,rightRange)
minHeap = []
for i in range(leftRange,rightRange+1):
    print(i)
    heapq.heappush(minHeap,(abs(arr[i]-x),arr[i]))
# print(minHeap)
res = []
print(res)
for _ in range(k):
    res.append(heapq.heappop(minHeap)[1])
print(res)