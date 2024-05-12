n = 3
x = 4
xB = bin(x).replace("0b", "00")
nB = bin(n).replace("0b", "00")
# print(bin(n).replace("0b","00"))
# print(bin(x).replace("0b","00"))
print(xB,nB)
for i in xB:
    print(i)
