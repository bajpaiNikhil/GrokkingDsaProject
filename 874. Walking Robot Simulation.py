commands = [4, -1, 4, -2, 4]
obstacles = [[2, 4]]

obstaclesSet = set()
currentPointingDirection = 0
maxDistance = 0

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for obsX, obsY in obstacles:
    obstaclesSet.add((obsX, obsY))
print(obstaclesSet)

x, y = 0, 0
for command in commands:
    print(command)
    if command == -2:
        currentPointingDirection = (currentPointingDirection - 1) % 4
    elif command == -1:
        currentPointingDirection = (currentPointingDirection + 1) % 4
    else:
        dx, dy = directions[currentPointingDirection]
        print(dx, dy, x, y)
        for ii in range(command):
            distanceX, distanceY = x + dx, y + dy
            print("-", "i=",ii ,distanceX, distanceY, x, y, obstaclesSet)
            if (x + dx, y + dy) in obstaclesSet:
                print('Here', "-", distanceX, distanceY, x, y)
                break
            x = distanceX
            y = distanceY
        maxDistance = max(maxDistance, x * x + y * y)
        print(maxDistance)
        print(x, y)
print(maxDistance)
