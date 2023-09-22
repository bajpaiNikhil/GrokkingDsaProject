



nums1 = [55,30,5,4,2]
nums2 = [100,20,10,10,5]

pointerOne = 0
pointerTwo = 0
maxValid = 0
while pointerOne != len(nums1) and pointerTwo != len(nums2):
    # print(nums1[pointerOne],nums2[pointerTwo])
    if nums1[pointerOne] > nums2[pointerTwo]:
        pointerOne+=1
    else:
        maxValid = max(maxValid,(pointerTwo-pointerOne))
        pointerTwo+=1
print(maxValid)
