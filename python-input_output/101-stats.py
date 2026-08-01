#!/usr/bin/python3
"""Script that computes metrics from stdin."""

import sys

valid_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}

total_size = 0
line_count = 0


def print_stats():
    """Print accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(valid_codes.keys()):
        if valid_codes[code]:
            print("{}: {}".format(code, valid_codes[code]))


try:
    for line in sys.stdin:
        try:
            parts = line.split()
            status = parts[-2]
            size = int(parts[-1])

            total_size += size

            if status in valid_codes:
                valid_codes[status] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_stats()

        except (IndexError, ValueError):
            continue

except KeyboardInterrupt:
    print_stats()
    raise

print_stats()
