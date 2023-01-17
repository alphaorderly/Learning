from typing import List

def rec(dp, cost, n):
    if n < 0: return 0
    if dp[n] != 0: return dp[n]
    dp[n] = min(cost[n] + rec(dp, cost, n-1), cost[n] + rec(dp, cost, n-2))
    return dp[n]

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost))
        cost = cost
        dp[0] = cost[0]
        dp[1] = cost[1]
        return min(rec(dp, cost, len(dp)-1), rec(dp, cost, len(dp)-2))

s = Solution()

s.minCostClimbingStairs([1, 2, 3, 4, 5, 6, 7])