from typing import List

def search(grid: List[List[int]], vert: int, hori: int, vertSize: int, horiSize: int):
    mv = [-1, 0, 1, 0]
    mh = [0, -1, 0, 1]
    grid[vert][hori] = 2

    count = 1
    for i in range(4):
        tv = vert + mv[i]
        th = hori + mh[i]
        if tv < 0 or tv >= vertSize or th < 0 or th >= horiSize or grid[tv][th] != 1: continue
        count += search(grid, tv, th, vertSize, horiSize)
    
    return count


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count = max(count, search(grid, i, j, len(grid), len(grid[0])))
        return count

s = Solution()

s.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])