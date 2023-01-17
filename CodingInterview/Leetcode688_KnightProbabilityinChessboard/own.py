
# 움직였을때 살아남는 경우의 수를 적어줌
def knightMoves(n: int, row: int, col: int):
    mx = [-2, -2, 2, 2, 1, -1, 1, -1]
    my = [-1, 1, -1, 1, -2, -2, 2, 2] 
    cnt = 0
    for i in range(8):
        tx = row + mx[i]
        ty = col + my[i]
        if tx >= 0 and tx < n and ty >= 0 and ty < n: cnt += 1
    return cnt

def knightProb(n, k, row, col, board, turn = 8):
    if k == 0: return 1.0

    # memoization 되어 있는 확률
    if k != 1 and board[k][row][col] != 0:
        return board[k][row][col]

    mx = [-2, -2, 2, 2, 1, -1, 1, -1]
    my = [-1, 1, -1, 1, -2, -2, 2, 2]

    # 마지막 자리일떄 확률
    if k == 1:
        return board[k][row][col] / turn

    prob = 0
    for i in range(8):
        tx = row + mx[i]
        ty = col + my[i]
        if tx >= 0 and tx < n and ty >= 0 and ty < n: prob += knightProb(n, k-1, tx, ty, board, turn * 8)
    board[k][row][col] = prob
    return board[k][row][col]



class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        board = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(101)]
        for i in range(len(board[0])):
            for j in range(len(board[0][0])):
                board[1][i][j] = knightMoves(n, i, j)
        
        return knightProb(n, k, row, column, board)

s = Solution()

print(s.knightProbability(8, 30, 6, 4))
