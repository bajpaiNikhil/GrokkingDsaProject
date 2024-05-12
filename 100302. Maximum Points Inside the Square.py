points = [[2, 2], [-1, -2], [-4, 4], [-3, 1], [3, -3]]
s = "abdca"


# Sort the points based on the maximum absolute value
sorted_points = sorted(points, key=lambda point: max(abs(point[0]), abs(point[1])))
print(sorted_points)