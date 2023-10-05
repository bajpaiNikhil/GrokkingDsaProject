tokens = [100, 200, 300, 400]
power = 200

tokens.sort()
left = 0
right = len(tokens) - 1

ans = 0
score = 0

while left <= right:
    if power >= tokens[left]:
        score += 1
        power -= tokens[left]
        ans = max(ans, score)
        left += 1
    elif power < tokens[left] and score > 0:
        score -= 1
        power += tokens[right]
        right -= 1
    else:
        print(ans)
        break
print(ans)
