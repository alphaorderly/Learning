class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost = [0] + cost
        dp = [0 for _ in range(len(cost))]
        dp[1] = cost[1]
        dp[2] = cost[2]
        for j in range(3, len(cost)):
            dp[j] = min(dp[j-2] + cost[j], dp[j-1] + cost[j])
        return min(dp[len(dp)-1], dp[len(dp)-2])