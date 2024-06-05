import heapq

# matrix = [[1,5,9],[10,11,13],[12,13,15]]
# K=8
matrix = [[1,2],[3,4]]
k= 2

minHeap = []
for i in range(len(matrix)):
    # print((matrix[i][0],0,list[i]),i)
    heapq.heappush(minHeap, (matrix[i][0],0,matrix[i]))
print(minHeap)

numberCount , number = 0,0

while minHeap:
    number,index , listIs = heapq.heappop(minHeap)
    print(number,index,listIs,len(listIs),index+1,number,numberCount)
    numberCount+=1
    if numberCount == k:
        break
    if len(listIs) > index+1:
        heapq.heappush(minHeap,(listIs[index+1],index+1,listIs))
print(number)

