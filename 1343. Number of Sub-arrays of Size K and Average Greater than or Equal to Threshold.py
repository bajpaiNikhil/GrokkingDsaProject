

arr = [11,13,17,23,29,31,7,5,2,3]
k = 3
threshold = 5

windowStart = 0
windowTh = 0
count = 0
for windowEnd in range(len(arr)):
    windowTh+=arr[windowEnd]
    if windowEnd >= k-1:
        if(windowTh//k)>=threshold:
            # print("b",windowEnd,windowStart,windowTh,arr[windowStart:windowEnd])

            count+=1
            windowTh -= arr[windowStart]
            windowStart+=1
            # print("a",windowEnd,windowStart,windowTh,arr[windowStart:windowEnd])
        else:
            windowTh -= arr[windowStart]
            windowStart+=1

print(count)
