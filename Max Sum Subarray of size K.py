Arr = [1, 2, 3, 4]
k = 2

wSum = 0
maxSum = 0
wStart = 0
for wEnd in range(len(Arr)):
    wSum += Arr[wEnd]
    if wEnd - wStart + 1 == k:
        maxSum = max(maxSum, wSum)
        wSum -= Arr[wStart]
        wStart += 1
print(maxSum)
