n,m,k = map(int,input().split())
# print(n,m,k)
count= 0
for _ in range(1,k+1):
    studentAndThereQuestion = list(map(int, input().split()))
    # print(studentAndThereQuestion[:-1])
    if sum(studentAndThereQuestion[:-1]) >m and studentAndThereQuestion[-1] <10:
        count+=1
print(count)