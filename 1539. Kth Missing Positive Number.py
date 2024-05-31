
arr = [2,3,4,7,11]
k = 5

i = 0
while i<len(arr):
    j = arr[i]-1

    if 0< arr[i]<= len(arr) and arr[i]!=arr[j]:
        arr[i],arr[j] = arr[j],arr[i]
    else:
        i+=1
print(arr)
missingNumber = []
extraNumber= set()

for i in range(len(arr)):
    if len(missingNumber)<k:
        if arr[i] != i+1:
            missingNumber.append(i+1)
            extraNumber.add(arr[i])

a = 1
while len(missingNumber)< k:
    candidateNUmber = a + len(arr)
    if candidateNUmber not in extraNumber:
        missingNumber.append(candidateNUmber)
    a+=1
print(missingNumber[k-1])
