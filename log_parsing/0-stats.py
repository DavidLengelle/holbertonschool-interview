#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""

import sys


def print_stats(total_size, status_counts):
    """Print the accumulated file size and status code counts"""

    print("File size: {}".format(total_size))
    for code in sorted(status_counts):
        print("{}: {}".format(code, status_counts[code]))


if __name__ == "__main__":
    total_size = 0
    status_counts = {}
    count = 0

    try:
        for line in sys.stdin:
            parts = line.split()

            try:
                size = int(parts[-1])
                code = parts[-2]
            except (IndexError, ValueError):
                continue

            total_size += size

            if code in status_counts:
                status_counts[code] += 1
            else:
                status_counts[code] = 1

            count += 1

            if count % 10 == 0:
                print_stats(total_size, status_counts)

        print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise
