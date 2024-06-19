import heapq

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
maxHeap = []
res = []
for i in range(len(nums)):
    heapq.heappush(maxHeap, (-nums[i], i))
    # Ensure that we only start recording results once we've hit the window size k
    if i >= k - 1:
        print("1", maxHeap)
        # Remove elements not within the sliding window
        while maxHeap[0][1] <= i - k:
            heapq.heappop(maxHeap)
        # The current maximum is the negation of the root of the heap
        res.append(-maxHeap[0][0])
print(maxHeap)
print(res)
