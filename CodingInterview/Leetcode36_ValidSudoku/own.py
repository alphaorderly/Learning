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

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.' and checkcorrect(board, i, j) == False: return False
        return True