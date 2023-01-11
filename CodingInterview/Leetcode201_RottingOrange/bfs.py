from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        st = list()
        vertSize = len(grid)
        horiSize = len(grid[0])
    
        mv = [-1, 0, 1, 0]
        mh = [0, -1, 0, 1]

        freshOrange = 0

        cnt = 0

        # 초기 확인, 썩어있는 오렌지의 위치들과 멀쩡한 오렌지들의 갯수를 알아낸다.
        for v in range(vertSize):
            for h in range(horiSize):
                if grid[v][h] == 1:
                    freshOrange += 1
                elif grid[v][h] == 2:
                    st.append([v, h])

        while len(st) != 0 and freshOrange != 0:
            # 새로이 썩은 오렌지들의 위치를 저장한다.
            newRotten = []

            # 기존에 썩어있던 오렌지들을 전부 전이시킨다.
            while len(st) != 0:
                place = st.pop()
                for i in range(4):
                    tv = place[0] + mv[i]
                    th = place[1] + mh[i]
                    if tv < 0 or tv >= vertSize or th < 0 or th >= horiSize or grid[tv][th] != 1: continue
                    grid[tv][th] = 2
                    newRotten.append([tv, th])
                    freshOrange -= 1
            cnt += 1

            # 새로 썩은 오렌지들이 전이할수 있도록 해준다.
            st.extend(newRotten)

        # 오렌지를 썩일만큼 썩였는데 아직도 싱싱한게 남아있으면 더이상 진행이 불가능하기에 -1 리턴, 이외엔 cnt 리턴하면 된다.
        if freshOrange != 0:
            return -1
        else:
            return cnt

s = Solution()

print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))