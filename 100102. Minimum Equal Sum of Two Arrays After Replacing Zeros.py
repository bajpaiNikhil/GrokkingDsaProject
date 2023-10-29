

nums1 = [2,0,2,0]
nums2 = [1,4]

sum1= 0
zero1 = 0
sum2 = 0
zero2 = 0

for i in nums1:
    sum1 += i
    if i == 0:
        sum1 += 1

for j in nums2:
    sum2 += j
    if j == 0:
        sum2 += 1

if sum2 == sum1:
    print(sum1)
elif sum1 < sum2 and 0 in nums1:
    print(sum2)
elif sum2 < sum1 and 0 in nums2:
    print(sum1)
else:
    print(-1)