n = 7
bit_count = 0
a= n
while n> 0:
    bit_count += 1
    n>>=1
print(bit_count)
all_bit_set = pow(2,bit_count)-1
print(bit_count,all_bit_set)
print(a^all_bit_set)