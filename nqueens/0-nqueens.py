#!/usr/bin/python3
"""Solve the N queens puzzle"""

import sys


def is_safe(positions: list, row: int, col: int) -> bool:
    """Return True if no placed queen attacks the given square"""

    for r in range(row):
        c = positions[r]
        if c == col:
            return False
        if abs(r - row) == abs(c - col):
            return False
    return True


def solve(positions: list, row: int, n: int, solutions: list) -> None:
    """Find every solution by placing one queen per row"""

    if row == n:
        solution = []
        for i in range(n):
            solution.append([i, positions[i]])
        solutions.append(solution)
        return
    for col in range(n):
        if is_safe(positions, row, col):
            positions.append(col)
            solve(positions, row + 1, n, solutions)
            positions.pop()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    positions = []
    solutions = []
    solve(positions, 0, n, solutions)
    for solution in solutions:
        print(solution)
