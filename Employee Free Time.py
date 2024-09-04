import heapq

employeeTime = [[[1, 3], [5, 6]], [[2, 3], [6, 8]]]

minHeap = []
result = []

for i, employee in enumerate(employeeTime):
    # print(i,employee,employee[0])
    heapq.heappush(minHeap, (employee[0][0], i, 0))
print(minHeap)
previous = employeeTime[minHeap[0][1]][minHeap[0][2]][0]
print(minHeap[0], minHeap[0][1], employeeTime[minHeap[0][1]], employeeTime[minHeap[0][1]][minHeap[0][2]][0])
print(previous)
start, i, j = heapq.heappop(minHeap)
interval = employeeTime[i][j]

# If there's a gap between the previous end and the current start, add to result
if interval[0] > previous:
    result.append([previous, interval[0]])

previous = max(previous, interval[-1])

# If there's a next interval for the current employee, add it to the heap
if j + 1 < len(employeeTime[i]):
    next_interval = employeeTime[i][j + 1]
    heapq.heappush(minHeap, (next_interval[0], i, j + 1))
print(result)
