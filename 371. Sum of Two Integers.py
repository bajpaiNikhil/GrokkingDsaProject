a = -1  # 00010
b = 1  # 00011
while b:
    carry = a & b
    print( carry )
    a = a ^ b
    print(a)
    b = carry << 1
    print(b)
print(a)
