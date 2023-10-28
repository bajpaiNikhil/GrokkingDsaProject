

arr = [1,2,3,5]
k = 3

left = 0
right = 1
def check (arr,mid):
    count = 0
    p, q = 0, 0
    maxFraction = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            factionIs = arr[i]/arr[j]
            if factionIs <= mid:
                count+=len(arr)-j

                if( arr[i]/arr[j] )> maxFraction:
                    maxFraction =  arr[i]/arr[j]
                    p ,q = arr[i],arr[j]
                break
    return count , [p,q]

while left< right:
    mid = left + (right -left)/2
    count , result = check(arr,mid)
    if count == k :
        print(result)
        break
    elif count >k:
        right = mid
    else:
        left = mid
print([])