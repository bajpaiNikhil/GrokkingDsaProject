import heapq

n = 12
primes = [2,7,13,19]

heap = [1]
uniqueSet = set()
while n-1 :
    poppedElement = heapq.heappop(heap)

    for i in primes:
        if poppedElement*i not in uniqueSet:
            heapq.heappush(heap, poppedElement * i)
            uniqueSet.add(poppedElement * i)
    n-=1
print(heap)
