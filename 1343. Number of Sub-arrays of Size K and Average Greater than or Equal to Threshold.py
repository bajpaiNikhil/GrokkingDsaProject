
arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
i= 0
j = 0
windowTh = 0
count = 0

while j<len(arr):
    windowTh +=arr[j]
    if j-i+1<k:
        j+=1
    elif j-i+1==k:
        th = windowTh//k
        if th >=threshold:
            count+=1
        windowTh-=arr[i]
        i+=1
        j+=1
print(count)