from typing import List

from collections import deque


def count(bombs: List[List[int]], start: int, gc):
    check = [0 for _ in range(len(bombs))]
    q = deque()

    count = 0

    q.append([bombs[start], start])
    check[start] = 1
    gc[start] = 1

    while len(q) != 0:
        node = q.popleft()
        check[node[1]] = 1
        gc[node[1]] = 1
        count += 1
        x = node[0][0]
        y = node[0][1]
        r = node[0][2]
        for i, v in enumerate(bombs):
            if check[i] == 0 and ((x - v[0])**2 + (y-v[1])**2)**0.5 <= r:
                q.append([v, i])
                check[i] = 1
                gc[i] = 1

    return count

        

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        cnt = 1
        gc = [0 for _ in range(len(bombs))]
        for i in range(len(bombs)):
            if gc[i] == 1: continue
            cnt = max(cnt, count(bombs, i, gc))
        return cnt

s = Solution()

print(s.maximumDetonation([[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]))