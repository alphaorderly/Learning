class Solution(object):
    # 버킷 정렬
    def bucketSort(self, nums):
        for i in range(7):
            bucket = [[], [], [], [], [], [], [], [], [], []]
            for num in nums:
                bucket[(num // (10**i)) % 10].append(num)
            idx = 0
            for b in range(9, -1, -1):
                for c in bucket[b]:
                    nums[idx] = c
                    idx += 1
        return nums

    def findKthLargest(self, nums, k):
        np = [x + 100000 for x in nums]
        return self.bucketSort(np)[k-1] - 100000
        

s = Solution()

s.findKthLargest([1, 55, 23, 6, 122, 4], 4)