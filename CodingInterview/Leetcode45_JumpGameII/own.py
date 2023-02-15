from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i in range(len(nums)-1):
            for j in range(1, nums[i]+1):
                if i + j >= len(nums): break
                if dp[i+j] == 0: dp[i+j] = dp[i] + 1
                elif dp[i] + 1 < dp[i+j]: dp[i+j] = dp[i] + 1
        return dp.pop()

s = Solution()

s.jump([2,1])