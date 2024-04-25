import heapq

nums = ["the","day","is","sunny","the","the","the","sunny","is","is"]

k = 4
dic = {}
for i in nums:
    if i not in dic:
        dic[i] = 0
    dic[i]+=1
print(dic)
unique_nums = list(dic.keys())
print(unique_nums)
heap = [(dic[i],i) for i in unique_nums[:k] ]
print(heap)
heapq.heapify(heap)
print(heap)
for i in unique_nums[k:]:
    heapq.heappushpop(heap ,(dic[i],i))
print(heap)
print([i[1] for i in heap])
