from typing import List

from copy import deepcopy as dc

ans = list()

def search(nums: List[int], acc: List[int], n: int):
    global ans
    if n >= len(nums): return 
    if len(acc) == 0 or acc[len(acc)-1] <= nums[n]: 
        acc.append(nums[n])
    if len(acc) > 1 and acc not in ans:
        ans.append(dc(acc))
    for i in range(n+1, len(nums)):
        search(nums, dc(acc), i)

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        global ans
        ans = []
        for i in range(len(nums)):
            search(nums, [], i)
        return ans       

s = Solution()
print(s.findSubsequences([4, 6, 7, 7]))