#!/usr/bin/python3
"""Pascal Triangle module"""


def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle of n"""

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(n - 1):
        new_row = [1]
        prev_row = triangle[-1]

        for j in range(len(prev_row) - 1):
            new_row.append(prev_row[j] + prev_row[j + 1])

        new_row.append(1)
        triangle.append(new_row)

    return triangle
