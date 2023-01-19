from typing import List
import math


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        def comb(n, r):
            return math.factorial(n) // (math.factorial(n-r) * math.factorial(r))
        dp = [0] * (len(nums))
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = dp[i-1] + nums[i]

        count = 0

        lst = [0] * k
        
        for i in range(len(dp)):
            lst[dp[i]%k] += 1

        print(lst)

        for i in lst:
            if i > 1:
                count += comb(i, 2)
        
        return count + lst[0]


s = Solution()

print(s.subarraysDivByK([4,5,0,-2,-3,1], 5))