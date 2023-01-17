from collections import deque
from typing import List

def beautifulPrint(lst: List[List[int]]):
    print('--------------------------------------------------')
    for i in lst:
        print(i)
    print('--------------------------------------------------')


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        vertSize = len(rooms)
        horiSize = len(rooms[0])

        mv = [-1, 0, 1, 0]
        mh = [0, -1, 0, 1]

        gates = deque()

        # 들어갈수 있는 Gate들 전부 조사함.
        for v in range(vertSize):
            for h in range(horiSize):
                if rooms[v][h] == 0:
                    gates.append([v, h])

        while len(gates) != 0:
            # 순회 위해 빼옴
            gate = gates.popleft()
            for i in range(4):
                tv = gate[0] + mv[i]
                th = gate[1] + mh[i]
                if tv < 0 or tv >= vertSize or th < 0 or th >= horiSize or rooms[tv][th] == 0 or rooms[tv][th] == -1: continue
                # 적혀있는 거리보다 우리가 더 가까운 경우
                if rooms[tv][th] > rooms[gate[0]][gate[1]] + 1:
                    rooms[tv][th] = rooms[gate[0]][gate[1]] + 1
                    gates.append([tv, th])
        return rooms


s = Solution()

print(s.wallsAndGates([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]))

        