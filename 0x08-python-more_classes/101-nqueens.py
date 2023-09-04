#!/usr/bin/python3
"""A program that solves the N queens problem."""
import sys


class NQueensSolver:
    def __init__(self, N):
        self.N = N
        self.board = [-1] * N

    def is_safe(self, row, col):
        for i in range(row):
            if self.board[i] == col or \
                    self.board[i] - i == col - row or \
                    self.board[i] + i == col + row:
                return False
        return True

    def solve(self, row):
        if row == self.N:
            print([[i, self.board[i]] for i in range(self.N)])
        else:
            for col in range(self.N):
                if self.is_safe(row, col):
                    self.board[row] = col
                    self.solve(row + 1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        SIZE = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if SIZE < 4:
        print("N must be at least 4")
        sys.exit(1)

    solver = NQueensSolver(SIZE)
    solver.solve(0)
