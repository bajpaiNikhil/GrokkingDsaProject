nums = [10,1,2,7,1,3]
p = 2
nums.sort()
def check (mid , nums, p):
    count = 0
    i = 0
    while i < len(nums)-1:
        if abs(nums[i]-nums[i+1]) <= mid:
            count+=1
            i +=2
        else:
            i+=1
        if count == p:
            return True
    return False

left = 0
right = 10**9
ans= 0
while left<= right:
    mid = left+(right-left)//2

    if check(mid,nums,p):
        ans = mid
        right = mid-1
    else:
        left = mid+1
print(ans)