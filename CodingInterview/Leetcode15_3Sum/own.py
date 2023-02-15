from typing import List, Set, Tuple


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        dct: Set[Tuple] = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) * -1 in dct:
                    dct[(nums[i] + nums[j]) * -1].add((i, j))
                else:
                    dct[(nums[i] + nums[j]) * -1] = {(i, j)}
        for x in range(len(nums)):
            if nums[x] not in dct: continue
            for y in dct[nums[x]]:
                if x in y: continue
                ans.add(tuple(sorted([nums[y[0]], nums[y[1]], nums[x]])))
        return [list(x) for x in ans]

s = Solution()

print(s.threeSum([-1,0,1,2,-1,-4]))