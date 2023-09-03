

arr = [1,2,3,4,5]
k = 2

arr.sort()
median = arr[(len(arr)-1)//2]
left  = 0
right = len(arr)-1

while len(arr)+left-right<=k:
    print(arr[:left] + arr[right + 1:])
    if median-arr[right] > arr[left] -median :
        left +=1
    else:
        right-=1
print(arr[:left]+arr[right+1:])