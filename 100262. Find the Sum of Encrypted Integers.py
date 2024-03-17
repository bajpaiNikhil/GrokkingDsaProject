nums = [109]
sum = 0
for i in nums:
    # print(i)
    if len(str(i)) == 1:
        sum+=i
    else:
        a = str(i)
        b = max(a)
        # print(a,b)
        sum+= int(b * len(str(i)))
print(sum)