from typing import List

from copy import deepcopy as cp

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        p = []
        # 백트래킹 함수
        def backtrack(numbers: List[int], i: int):
            # 길이가 1보다 크면 기록에 남긴다.
            if len(p) > 1:
                ans.append(cp(p))

            # 숫자 이어나감
            for j in range(i, len(numbers)):
                # 비어있거나 숫자가 줄어들면 X
                if p and p[-1] > numbers[j]: continue

                if j > i and numbers[j] in numbers[i:j]: continue

                # 백트래킹 추가 -> recursive -> 빼기
                p.append(nums[j])
                backtrack(numbers, j+1)
                p.pop()
        backtrack(nums, 0)
        print(ans)
        return ans

s = Solution()
s.findSubsequences([4, 6, 7, 7])