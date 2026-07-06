# Island Perimeter

Given a grid of water and land, compute the **perimeter of the island** it
describes.

The grid is a list of lists of integers:

- `0` represents water.
- `1` represents land.
- Each cell is square, with a side length of `1`.
- Cells are connected horizontally and vertically only (never diagonally).
- The grid is completely surrounded by water.
- There is exactly one island (or none).
- The island has no lakes (water inside that is not connected to the water
  around the island).

## Task

Complete the function `island_perimeter(grid)` that returns the perimeter of the
island described in `grid`.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Code should use the `pycodestyle` style (version 1.7.x)
- All modules and functions must be documented
- No module is allowed to be imported
- All files must be executable

## Approach

Walk through every cell of the grid. For each land cell (`1`), count how many of
its four sides are **exposed**.

A side is exposed when the neighbour on that side is water, or when there is no
neighbour at all because the cell sits on the edge of the grid. Adding up every
exposed side over the whole grid gives the perimeter.

For each side, the position is checked **before** reading the neighbour. This
avoids a classic Python pitfall: a negative index (like `grid[-1]`) does not
raise an error, it silently wraps around to the end of the list and would give a
wrong result.

```
top    -> r == 0                or grid[r - 1][c] == 0
bottom -> r == len(grid) - 1    or grid[r + 1][c] == 0
left   -> c == 0                or grid[r][c - 1] == 0
right  -> c == len(grid[0]) - 1 or grid[r][c + 1] == 0
```

Time complexity: `O(rows * cols)`.

## Prototype

```python
def island_perimeter(grid):
```

## Usage

```python
#!/usr/bin/python3
island_perimeter = __import__('0-island_perimeter').island_perimeter

grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))
```

Output:

```
12
```

## Files

| File                     | Description                     |
| ------------------------ | ------------------------------- |
| `0-island_perimeter.py`  | The `island_perimeter` function |

## Author

David Lengelle - Holberton School
