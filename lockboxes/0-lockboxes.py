#!/usr/bin/python3
"""Lockboxes module"""


def canUnlockAll(boxes):
    """Return True if all the boxes can be opened, False otherwise"""
    opened = {0}
    to_check = [0]

    while len(to_check) > 0:
        current = to_check.pop()
        for key in boxes[current]:
            if key < len(boxes) and key not in opened:
                opened.add(key)
                to_check.append(key)

    if len(opened) == len(boxes):
        return True
    else:
        return False
