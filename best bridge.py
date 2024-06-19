"""
best bridge
Write a function, bestBridge, that takes in a grid as an argument. The grid contains water (W) and land (L). There are exactly two islands in the grid. An island is a vertically or horizontally connected region of land. Return the minimum length bridge needed to connect the two islands. A bridge does not need to form a straight line.

test_00:
const grid = [
  ["W", "W", "W", "L", "L"],
  ["L", "L", "W", "W", "L"],
  ["L", "L", "L", "W", "L"],
  ["W", "L", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
];
bestBridge(grid); // -> 1
test_01:
const grid = [
  ["W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
  ["L", "L", "W", "W", "L"],
  ["W", "L", "W", "W", "L"],
  ["W", "W", "W", "L", "L"],
  ["W", "W", "W", "W", "W"],
];
bestBridge(grid); // -> 2
test_02:
const grid = [
  ["W", "W", "W", "W", "W"],
  ["W", "W", "W", "L", "W"],
  ["L", "W", "W", "W", "W"],
];
bestBridge(grid); // -> 3
test_03:
const grid = [
  ["W", "W", "W", "W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W", "L", "W", "W"],
  ["W", "W", "W", "W", "L", "L", "W", "W"],
  ["W", "W", "W", "W", "L", "L", "L", "W"],
  ["W", "W", "W", "W", "W", "L", "L", "L"],
  ["L", "W", "W", "W", "W", "L", "L", "L"],
  ["L", "L", "L", "W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W", "W", "W", "W"],
];
bestBridge(grid); // -> 3
test_04:
const grid = [
  ["L", "L", "L", "L", "L", "L", "L", "L"],
  ["L", "W", "W", "W", "W", "W", "W", "L"],
  ["L", "W", "W", "W", "W", "W", "W", "L"],
  ["L", "W", "W", "W", "W", "W", "W", "L"],
  ["L", "W", "W", "W", "W", "W", "W", "L"],
  ["L", "W", "W", "W", "W", "W", "W", "L"],
  ["L", "W", "W", "L", "W", "W", "W", "L"],
  ["L", "W", "W", "W", "W", "W", "W", "L"],
  ["L", "W", "W", "W", "W", "W", "W", "L"],
  ["L", "W", "W", "W", "W", "W", "W", "L"],
  ["L", "W", "W", "W", "W", "W", "W", "L"],
  ["L", "L", "L", "L", "L", "L", "L", "L"],
];
"""
from collections import deque


def inBound(grid, row, col):
    rowInbound = 0 <= row < len(grid)
    colInbound = 0 <= col < len(grid[0])
    return rowInbound and colInbound


def traverseIsland(grid, row, col, visited):
    if not inBound(grid, row, col) or grid[row][col] == "W":
        return visited
    position = f"{row},{col}"
    if position in visited:
        return visited
    visited.add(position)

    traverseIsland(grid, row - 1, col, visited)
    traverseIsland(grid, row + 1, col, visited)
    traverseIsland(grid, row, col - 1, visited)
    traverseIsland(grid, row, col + 1, visited)
    return visited


def bestBridge(grid):
    mainIsland = set()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            potentialIsland = traverseIsland(grid, row, col, set())
            if len(potentialIsland) > 0:
                mainIsland = potentialIsland
                break

    visited = mainIsland
    print(mainIsland)
    queue = deque()
    for pos in mainIsland:
        row, col = map(int, pos.split(','))
        queue.append((row, col, 0))
    while queue:
        r, c, distance = queue.popleft()
        for deltaRow, deltaCol in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            newRow, newCol = r + deltaRow, c + deltaCol
            newPos = f"{newRow},{newCol}"
            if inBound(grid, newRow, newCol) and newPos not in visited:
                if grid[newRow][newCol] == "L" and newPos not in mainIsland:
                    return distance
                queue.append((newRow, newCol, distance + 1))
                visited.add(newPos)
    return -1


grid = [
    ["W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W", "L", "W", "W"],
    ["W", "W", "W", "W", "L", "L", "W", "W"],
    ["W", "W", "W", "W", "L", "L", "L", "W"],
    ["W", "W", "W", "W", "W", "L", "L", "L"],
    ["L", "W", "W", "W", "W", "L", "L", "L"],
    ["L", "L", "L", "W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W"],
]
print(bestBridge(grid))
