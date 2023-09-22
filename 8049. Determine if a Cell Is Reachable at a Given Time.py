

def canTransform(sx, sy, fx, fy, t):
    # Calculate the Manhattan distance between start and finish points
    distance = abs(fx - sx) + abs(fy - sy)

    if distance > t:
        return True

    if (t - distance) % 2 == 0:
        return True
    return False

# Example usage:
sx, sy, fx, fy, t = 3, 1, 7, 3, 3
print(canTransform(sx, sy, fx, fy, t))




