gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

result = 0
total = 0

if sum(gas)<sum(cost):
    print(-1)
    exit()
for i in range(len(gas)):
    total+=gas[i]-cost[i]
    if total<0:
        total =0
        result = i+1
print(result)

#
# for i in range(len(gas)):
#     if sum(gas) < sum(cost):
#         print(-1)
#         exit()
#     else:
#         total += gas[i] - cost[i]
#         if total < 0:
#             total = 0
#             result = i + 1
# print(result)
