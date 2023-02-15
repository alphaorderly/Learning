from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [0] * 2 * n
        for i in range(n):
            ans[i * 2] = nums[i]
        for i in range(n, 2*n):
            ans[(i-n)*2+1] = nums[i]
        return ans;

s = Solution()

print(s.shuffle([1,2,3,4,4,3,2,1], 4))