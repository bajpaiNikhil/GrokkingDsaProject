import heapq
#
nums = [3, 2, 1, 5, 6, 4]
k = 2
minHeap = []
for i in range(k):
    heapq.heappush(minHeap,nums[i])
print(minHeap)

for i in range(k,len(nums)):
    if nums[i] > minHeap[0]:
        heapq.heappushpop(minHeap,nums[i])
print(minHeap[0])
# heapq._heapify_max(nums)
# print(nums)
# for i in range(1,len(nums)+1):
#     if i == k:
#         print("from ",heapq._heappop_max(nums))
#
#         break
#     heapq._heappop_max(nums)
#     print("from here",nums)
# heap = nums[:k]
# print(heap)
# heapq.heapify(heap)
# print(heap,nums,nums[k:])
# for n in nums[k:]:
#     print("before",heap,n)
#     print(heapq.heappushpop(heap, n))
#     print("after",heap,n)
# print(heap[0],heap)