from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 찾지 못하면 [-1, -1] 리턴됨.
        left = right = -1
        start = 0
        end = len(nums)-1
        # 값의 왼쪽 끝 위치를 찾기 위한 Binary search
        while start <= end:
            mid = (start + end) // 2
            if (nums[mid] == target) and ((mid > 0 and nums[mid-1] != target) or (mid == 0)):
                left = mid
                break
            elif nums[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1
        start = 0
        end = len(nums)-1
        # 값의 오른쪽 끝을 찾기 위한 Binary search
        while start <= end:
            mid = (start + end) // 2
            if (nums[mid] == target) and ((mid < len(nums)-1 and nums[mid+1] != target) or (mid == len(nums)-1)):
                right = mid
                break
            elif nums[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1
        return [left, right]

s = Solution()

print(s.searchRange([5,7,7,8,8,10], 6))