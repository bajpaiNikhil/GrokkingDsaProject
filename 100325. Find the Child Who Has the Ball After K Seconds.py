n = 3
k = 5
count = 0
position = 0
direction = 1

while count < k:
    position += direction
    if position == 0 or position == n - 1:
        direction *= -1
    count += 1
print(position)