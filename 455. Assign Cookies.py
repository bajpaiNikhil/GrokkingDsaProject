g = [10, 9, 8, 7]
s = [5, 6, 7, 8]

# 7,8,9,10
# 5,6,7,8
sPointer = 0
gPointer = 0

g.sort()
s.sort()
print(g,s)
count = 0
while sPointer <= len(s)-1 and gPointer <= len(g)-1:
    print(sPointer,gPointer,s,g)
    if s[sPointer] >= g[gPointer]:
        count += 1
        sPointer += 1
        gPointer += 1
    else:
        sPointer += 1
print(count)

# g.sort()
# s.sort()
# print(g)
# print(s)
# gPointer = len(g)-1
# sPointer = len(s)-1
# count = 0
# while gPointer>=0 and sPointer >= 0:
#     if s[sPointer] >= g[gPointer]:
#         count+=1
#         gPointer-=1
#         sPointer-=1
#     else:
#         gPointer-=1
# print(count)
