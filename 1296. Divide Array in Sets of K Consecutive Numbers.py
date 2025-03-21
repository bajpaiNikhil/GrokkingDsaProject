nums = [3,2,1,2,3,4,3,4,5,9,10,11]
k = 3
nums.sort()
frequencyMap = {}
res = []
for i in nums:
    frequencyMap[i] = frequencyMap.get(i,0)+1
print(frequencyMap)

i = 0
n = len(frequencyMap)-1
while i <n: