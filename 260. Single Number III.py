nums = [1,2,1,3,2,5]
n1XorN2 = 0

for i in nums:
    n1XorN2 ^= i
print(n1XorN2)
print(bin(n1XorN2))
rightmostSetBit = 1
while(rightmostSetBit & n1XorN2) == 0:
    rightmostSetBit = rightmostSetBit << 1
print(rightmostSetBit)

nums1, nums2 = 0,0
for i in nums:
    print(i&rightmostSetBit,i ,bin(i),bin(rightmostSetBit))
    # which bit is set
    if i & rightmostSetBit != 0:
        nums1^=i
    else:
        nums2^=i
print(nums1,nums2)


