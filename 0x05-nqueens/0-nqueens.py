#!/usr/bin/python3
import sys

def nqueens(n):
    def is_valid(board, row, col):
        for r, c in enumerate(board):
            if c == col or r + c == row + col or r - c == row - col:
                return False
        return True
    
    def solve(board, row):
        if row == n:
            print_board(board)
            return True
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                solve(board, row + 1)
                board[row] = -1
    
    def print_board(board):
        for r in range(n):
            row = ['.' for _ in range(n)]
            row[board[r]] = 'Q'
            print(' '.join(row))
        print()
    
    if not n.isdigit():
        print('N must be a number')
        sys.exit(1)
    
    n = int(n)
    if n < 4:
        print('N must be at least 4')
        sys.exit(1)
    
    board = [-1] * n
    solve(board, 0)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    nqueens(sys.argv[1])
