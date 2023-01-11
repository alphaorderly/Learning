from typing import List

def fillIsland(grid: List[List[str]], x: int, y: int, xSize: int, ySize: int):
    xm = [-1, 0, 1, 0]
    ym = [0, -1, 0, 1]
    grid[x][y] = '2'
    for i in range(4):
        xt = x + xm[i]
        yt = y + ym[i]
        if xt < 0 or xt >= xSize or yt < 0 or yt >= ySize or grid[xt][yt] != '1': continue
        fillIsland(grid, xt, yt, xSize, ySize)



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        xSize = len(grid)
        ySize = len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    fillIsland(grid, i, j, xSize, ySize)
                    cnt += 1
        return cnt

s = Solution()

print(s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))