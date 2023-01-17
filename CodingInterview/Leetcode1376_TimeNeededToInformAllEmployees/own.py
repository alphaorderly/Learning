from typing import List
from collections import deque


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        maxTime = 0
        graph = [list() for _ in range(n)]

        for i in range(n):
            if manager[i] == -1: continue
            graph[manager[i]].append(i)
        
        q = deque()
        q.append(headID)

        while len(q) != 0:
            node = q.popleft()
            for i in graph[node]:
                if informTime[i] != 0:
                    informTime[i] += informTime[node]
                    q.append(i)
                else:
                    if maxTime < informTime[node]:
                        maxTime = informTime[node]
        
        return maxTime


s = Solution()

s.numOfMinutes(4, 2, [3,3,-1,2], [0,0,162,914])