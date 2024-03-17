import heapq
nums = [1,2,2,1,2,3,1]
queries = [[1,2],[3,3],[4,2]]
n = len(nums)
marked = set()
answer = []

heap = [(value, i) for i, value in enumerate(nums)]
heapq.heapify(heap)

total_sum = sum(nums)

for index, k in queries:
    if index not in marked:
        marked.add(index)
        total_sum -= nums[index]

    while k > 0 and heap:
        value, idx = heapq.heappop(heap)
        if idx not in marked:
            marked.add(idx)
            total_sum -= value
            k -= 1

    answer.append(total_sum)

print(answer)