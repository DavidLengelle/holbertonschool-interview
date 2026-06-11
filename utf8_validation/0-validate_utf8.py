#!/usr/bin/python3
"""Determine if a data set is a valid UTF-8 encoding"""


def validUTF8(data):
    """Return True if data is a valid UTF-8 encoding else False"""

    n = 0
    for num in data:
        num = num & 0b11111111
        if n == 0:
            if num >> 7 == 0b0:
                n = 0
            elif num >> 5 == 0b110:
                n = 1
            elif num >> 4 == 0b1110:
                n = 2
            elif num >> 3 == 0b11110:
                n = 3
            else:
                return False
        else:
            if num >> 6 != 0b10:
                return False
            n = n - 1
    return n == 0
