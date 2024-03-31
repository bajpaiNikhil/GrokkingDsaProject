import math

k = 11
if k == 1:
    print(0)
else:
    a = int(math.sqrt(11))

    if a*(a+1)>k:
        print(a+a+1)
    else:
        print(2*a)
