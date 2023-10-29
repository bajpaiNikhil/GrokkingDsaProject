
arr = [1, 2, 1]

# n = len(arr)
# result = 0
#
# for i in range(len(arr)):
#     distinctCount = 0
#     visited = [False] * 101
#
#     for j in range(i, len(arr)):
#         print(j,arr[j])
#         if not visited[arr[j]]:
#             visited[arr[j]] = True
#             distinctCount += 1
#         result += distinctCount**2
#
# print(result)

n = len(arr)
subList = []
result = 0
for i in range(n):
    for j in range(i+1,n+1):
        # print(arr[i:j])
        result += len(set(arr[i:j]))**2
        # subList.append(arr[i:j])
        # print(subList)
    # result+=len(set(subList))**2
# print(subList)
print(result)




