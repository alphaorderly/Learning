class Solution:
    def quickFind(self, nums, start, end):
        i = start + 1
        j = end
        pivot = start
        pivotValue = nums[start]
        while i <= j:
            while i <= end and pivotValue > nums[i]:
                i += 1
            while j > start and pivotValue <= nums[j]:
                j -= 1
            if i<=j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        nums[j], nums[pivot] = nums[pivot], nums[j]
        return j

    def findKthLargest(self, nums: list[int], k: int) -> int:
        start = 0
        end = len(nums)-1
        k = len(nums) - k + 1
        while True:
            place = self.quickFind(nums, start, end)
            if place == k-1: return nums[k-1]
            elif place < k-1:
                start = place + 1
            else:
                end = place - 1
        
s = Solution()

print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4))