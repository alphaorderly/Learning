class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        group = (numRows-1)*2
        ans = ''
        for j in range(0, numRows):
            for i, v in enumerate(s):
                if i % group == j or i % group == group - j:
                    ans += v
        return ans

s = Solution()

print(s.convert("PAYPALISHIRING", 4))