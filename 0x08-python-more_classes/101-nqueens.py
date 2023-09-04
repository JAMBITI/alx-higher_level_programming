#!/usr/bin/python3
import sys


def is_safe(i, j, board):
    """Check if placing a queen at position (i, j) is safe on the board."""
    for row, col in board:
        if i == row or j == col or abs(i - row) == abs(j - col):
            return False
    return True


def solve_nqueens(n):
    """Solve the N-Queens problem."""
    if n < 4:
        print("N must be at least 4")
        return

    def backtrack(row, board):
        if row == n:
            solutions.append(board.copy())
            return

        for col in range(n):
            if is_safe(row, col, board):
                board.append((row, col))
                backtrack(row + 1, board)
                board.pop()

    solutions = []
    backtrack(0, [])

    return solutions

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

n = int(sys.argv[1])
if not isinstance(n, int):
    print("N must be a number")
    sys.exit(1)

result = solve_nqueens(n)
for solution in result:
    print(solution)
