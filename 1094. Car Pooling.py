import heapq

trips = [[2,1,5],[3,3,7]]
capacity = 4

trips.sort(key = lambda t : t[1])
print(trips)

currPass =  0
minheap = [] # [end , passengers]
for t in trips :

    passengers, start , end = t

    while minheap and minheap[0][0] <= start:
        currPass-= minheap[0][1]
        heapq.heappop(minheap)
    currPass+=passengers

    if(currPass>capacity):
        print(False)
        exit()
    heapq.heappush(minheap,[end,passengers])
print(True)
