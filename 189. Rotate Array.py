nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

k%=len(nums)
print(len(nums),k,3%len(nums))
p1 = nums[:len(nums)-k]
p2 = nums[len(nums)-k:]
print(p1,p2)
print((p1[::-1]+p2[::-1])[::-1])