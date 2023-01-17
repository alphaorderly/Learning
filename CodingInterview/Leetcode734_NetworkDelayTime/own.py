
from typing import List

class Edge:
    def __init__(self, to: int, weight: int):
        self.to = to
        self.weight = weight

def getLeastDistance(check: List[int], distance: List[int]):
    min = 2 ** 32
    idx = -1
    for i, v in enumerate(distance):
        if min > v and check[i] == 0:
            min = v
            idx = i
    return idx


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = 2 ** 32 + 1
        graph = [list() for _ in range(n + 1)]
        check = [0 for _ in range(n + 1)]
        distance = [INF for _ in range(n + 1)]
 
        reachable = n - 1

        for t in times:
            graph[t[0]].append(Edge(t[1], t[2]))

        # 시작 정점 표 및 check
        check[k] = 1
        distance[k] = 0
        for g in graph[k]:
            distance[g.to] = g.weight
            

        while True: 
            # distance가 짧으면서 check되지 않은 정점 찾기
            start = getLeastDistance(check, distance)
            # 없으면 break
            if start == -1: break
            # 있으면 check 해서 다시 뽑히지 않도록 방지
            check[start] = 1
            reachable -= 1
            for v in graph[start]:
                # 이미 정점 체크가 끝나지 않은 정점에 한해 거쳐 가는게 빠른지 직접 가는게 빠른지 비교 후 대치.
                if check[v.to] == 0 and distance[v.to] > distance[start] + v.weight:
                    distance[v.to] = distance[start] + v.weight
        
        distance = distance[1:]
        
        if reachable == 0: return max(distance)
        else: return -1


s = Solution()

s.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)