#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):

    operations = 0
    d = 2

    if n <= 1:
        return 0

    while n > 1:
        while n % d == 0:
            operations += d
            n = n // d
        d += 1
    return operations
