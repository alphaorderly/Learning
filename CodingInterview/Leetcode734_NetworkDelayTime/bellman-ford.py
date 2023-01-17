from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = 2 ** 32
        distance = [INF for _ in range(n+1)]

        distance[k] = 0

        for _ in range(n-1):
            for edge in times:
                if distance[edge[1]] > distance[edge[0]] + edge[2]:
                    distance[edge[1]] = distance[edge[0]] + edge[2]

        distance = distance[1:]

        try:
            distance.index(INF)
            return -1
        except:
            return max(distance)

s = Solution()

s.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)