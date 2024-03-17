batteryPercentages = [1, 1, 2, 1, 3]
#
# print(max(batteryPercentages))
# count = 0
# for i in range(len(batteryPercentages)):
#     maxTillNow = max(batteryPercentages[i]-count,0)
#     if batteryPercentages[i] >= maxTillNow != 0:
#         count+=1
# print(count)

count = 0

for percentage in batteryPercentages:
    maxTillNow = max(percentage-count,0)
    if percentage >= maxTillNow != 0:
        count += 1

print(count)