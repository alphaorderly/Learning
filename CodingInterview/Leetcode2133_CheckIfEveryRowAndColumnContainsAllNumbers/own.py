from typing import List


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        def checker(matrix: List[List[int]], row: int, col: int, size: int):
            r = set()
            c = set()
            for i in range(size):
                if matrix[row][i] in r: return False
                if matrix[i][col] in c: return False
                r.add(matrix[row][i])
                c.add(matrix[i][col])
            return True
        for i in range(len(matrix)):
            if checker(matrix, i, i, len(matrix)) == False: return False
        return True