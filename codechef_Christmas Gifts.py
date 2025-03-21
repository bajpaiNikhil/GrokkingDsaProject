

t = int(input())
for t in range(t):
    h,l,w = map(int, input().split(" "))
    print(h,l,w)
    surfaceArea = 2*(l*w+l*h+w*h)
    numberOfGift = 1000//surfaceArea
    print(numberOfGift)