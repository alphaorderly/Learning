
from typing import List

def checkcorrect(board: List[List[str]], row, col):
    c = set()
    r = set()
    b = set()
    for i in board[row]:
        if i == '.': continue
        if i in r: return False
        r.add(i)
    for j in range(9):
        if board[j][col] == '.': continue
        if board[j][col] in c: return False
        c.add(board[j][col])
    trow = (row // 3) * 3
    tcol = (col // 3) * 3
    for i in range(trow, trow + 3):
        for j in range(tcol, tcol + 3):
            if board[i][j] == '.': continue
            if board[i][j] in b: return False
            b.add(board[i][j])
    return True

def sudoku(board: List[List[str]], empty, n):
    if n >= len(empty): 
        return 1
    for i in range(1, 10):
        board[empty[n][0]][empty[n][1]] = str(i)
        if checkcorrect(board, empty[n][0], empty[n][1]):
            x = sudoku(board, empty, n+1)
            if x == 1: return 1
        board[empty[n][0]][empty[n][1]] = '.'
        


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        empty = list()
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty.append([i, j])
        sudoku(board, empty, 0)
        print(board)


s = Solution()

s.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])