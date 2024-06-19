"""
closest carrot
Write a function, closestCarrot, that takes in a grid, a starting row, and a starting column.
In the grid, 'X's are walls, 'O's are open spaces, and 'C's are carrots.
The function should return a number representing the length of the shortest path
from the starting position to a carrot.
You may move up, down, left, or right, but cannot pass through walls (X).
If there is no possible path to a carrot, then return -1.

test_00:
const grid = [
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'X', 'O', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['O', 'X', 'C', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['C', 'O', 'O', 'O', 'O'],
];

closestCarrot(grid, 1, 2); // -> 4
test_01:
const grid = [
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'X', 'O', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['O', 'X', 'C', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['C', 'O', 'O', 'O', 'O'],
];

closestCarrot(grid, 0, 0); // -> 5
test_02:
const grid = [
  ['O', 'O', 'X', 'X', 'X'],
  ['O', 'X', 'X', 'X', 'C'],
  ['O', 'X', 'O', 'X', 'X'],
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'X', 'X', 'X', 'X'],
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'C', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O'],
];

closestCarrot(grid, 3, 4); // -> 9
test_03:
const grid = [
  ['O', 'O', 'X', 'O', 'O'],
  ['O', 'X', 'X', 'X', 'O'],
  ['O', 'X', 'C', 'C', 'O'],
];

closestCarrot(grid, 1, 4); // -> 2
test_04:
const grid = [
  ['O', 'O', 'X', 'O', 'O'],
  ['O', 'X', 'X', 'X', 'O'],
  ['O', 'X', 'C', 'C', 'O'],
];

closestCarrot(grid, 2, 0); // -> -1
"""
from collections import deque


def closestCarrot(grid, start, end):
    visited = set()
    visited.add(f"{start},{end}")
    queue = deque([(start, end, 0)])
    while queue:
        row, col, distance = queue.popleft()
        if grid[row][col] == 'C':
            return distance
        deltas = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for delta in deltas:
            deltaRow, deltaCol = delta
            neighbourRow = deltaRow + row
            neighbourCol = deltaCol + col
            rowInBound = 0 <= neighbourRow < len(grid)
            colInBound = 0 <= neighbourCol < len(grid[0])
            position = f"{neighbourRow},{neighbourCol}"
            if rowInBound and colInBound and position not in visited and grid[neighbourRow][neighbourCol] != "X":
                queue.append((neighbourRow, neighbourCol, distance + 1))
                visited.add(position)
    return -1


grid = [
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'X', 'O', 'O', 'O'],
    ['O', 'X', 'X', 'O', 'O'],
    ['O', 'X', 'C', 'O', 'O'],
    ['O', 'X', 'X', 'O', 'O'],
    ['C', 'O', 'O', 'O', 'O'],
]
print(closestCarrot(grid, 1, 2))
