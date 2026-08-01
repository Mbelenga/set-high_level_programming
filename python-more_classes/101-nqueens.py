#!/usr/bin/python3
"""Solve the N Queens problem."""

import sys


def is_safe(board, row, col):
    """Check if a queen can be placed at (row, col)."""
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve(board, row, n):
    """Solve the N Queens problem using backtracking."""
    if row == n:
        print([[r, board[r]] for r in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve(board, row + 1, n)


def main():
    """Validate arguments and start solving."""
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

    board = [-1] * n
    solve(board, 0, n)


if __name__ == "__main__":
    main()
