energy = [5, 2, -10, -5, 1]
k = 3
#
# sumEnergy = -float('inf')
#
# for i in range(len(energy)-1,len(energy)-k-1,-1):
#     currentSumEnergy = 0
#     for j in range(i,-1,-k):
#         # print(i,j,energy[i],energy[j])
#         currentSumEnergy += energy[j]
#         sumEnergy = max(sumEnergy,currentSumEnergy)
# print(sumEnergy)
#
# windowSum = sum(energy[-k:])
# print(windowSum)
#
# maxSum = windowSum
#
# for i in range(len(energy) - k - 1, -1, -1):
#     print(i, energy[i],energy[i+k])
#     windowSum += (energy[i] - energy[i + k])
#     print(windowSum)
#     maxSum = max(windowSum, maxSum)
#     print(maxSum)
# print(maxSum)

maxE = 0
for i in range(len(energy) - 1, -1, -k):
    maxE += max(0, energy[i])

print(maxE)