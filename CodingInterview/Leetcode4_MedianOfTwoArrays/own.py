from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        if len(nums3) % 2 == 1:
            return nums3[len(nums3) // 2]
        else:
            return (nums3[len(nums3) // 2 - 1] + nums3[len(nums3) // 2]) / 2

s = Solution()

print(s.findMedianSortedArrays([0, 1], [2, 3]))