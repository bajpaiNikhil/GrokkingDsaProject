
def count_divisors(n):
    odd_count = 0
    even_count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i % 2 == 1:
                odd_count += 1
            else:
                even_count += 1

            if n // i != i:
                if (n // i) % 2 == 1:
                    odd_count += 1
                else:
                    even_count += 1
        i += 1
    return odd_count, even_count


t= int(input())
for _ in range(t):
    n = int(input())
    oddCount ,evenCount = count_divisors(n)
    # print(oddCount,evenCount)
    if oddCount == evenCount:
        print(0)
    elif oddCount>evenCount:
        print(-1)
    else:
        print(1)


