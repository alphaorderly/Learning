from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        size = len(nums1) + len(nums2)
        idx1 = idx2 = 0
        res = []
        for i in range(size):
            if idx1 < len(nums1) and idx2 < len(nums2):
                if nums1[idx1] < nums2[idx2]:
                    res.append(nums1[idx1])
                    idx1 += 1
                else:
                    res.append(nums2[idx2])
                    idx2 += 1
            elif idx1 < len(nums1):
                res.append(nums1[idx1])
                idx1 += 1
            else:
                res.append(nums2[idx2])
                idx2 += 1
        if len(res) % 2 == 1:
            return res[len(res) // 2]
        else:
            return (res[len(res) // 2 - 1] + res[len(res) // 2]) / 2


s = Solution()

print(s.findMedianSortedArrays([1, 2, 3], [4]))