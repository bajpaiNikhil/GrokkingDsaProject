
n = int(input())
for _ in range(n):
    sizeOfList = int(input())
    numberOfStudent = list(map(int,input().split()))
    print(max(numberOfStudent)- min(numberOfStudent))