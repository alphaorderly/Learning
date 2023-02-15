class Solution:
    def countOdds(self, low: int, high: int) -> int:
        l = low % 2
        h = high % 2
        a = (high - low - 1) // 2
        if l == 0 and h == 0:
            return a + 1
        return (l == 1) + (h == 1) + a

s = Solution()

print(s.countOdds(3, 7))