from collections import defaultdict

nums1 = [1, 2, 4, 12]
nums2 = [2, 4]
k = 3
dic = defaultdict(int)
count = 0
for i in nums2:
    dic[i * k] += 1
print(dic)
for i in nums1:
    for j in dic:
        if i % j == 0:
            count += 1
print(count)
