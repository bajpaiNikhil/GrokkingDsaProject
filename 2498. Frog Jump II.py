
stones = [3,2,10,11,12]
n = len(stones)

if n == 2:
    print(stones[-1])  # So, last stone will be our answer.

diff_alternate_stone = 0  # Otherwise, the answer will be the max dist between alternate stones

for i in range(n - 2):  # We find all the alternate distances and maximize it.
    diff_alternate_stone = max(diff_alternate_stone, stones[i + 2] - stones[i])

print(diff_alternate_stone)