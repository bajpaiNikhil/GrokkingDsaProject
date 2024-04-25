import heapq

n = 5
start = 1

heap = [2]
uniqueUglyNumber = set()


while n-1:
    popped_element = heapq.heappop(heap)
    if popped_element*2 not in uniqueUglyNumber:
        heapq.heappush(heap,popped_element*2)
        uniqueUglyNumber.add(popped_element*2)
    if popped_element*11 not in uniqueUglyNumber:
        heapq.heappush(heap, popped_element * 11)
        uniqueUglyNumber.add(popped_element * 11)
    if popped_element*13 not in uniqueUglyNumber:
        heapq.heappush(heap,popped_element*13)
        uniqueUglyNumber.add(popped_element*13)
    n-=1
print(heapq.heappop(heap))
