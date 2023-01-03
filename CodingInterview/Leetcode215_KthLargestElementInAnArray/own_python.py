class Solution(object):
    def findKthLargest(self, nums: list, k):
        nums.sort(reverse=True)
        return nums[k-1]