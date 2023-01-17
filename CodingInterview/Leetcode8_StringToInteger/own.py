class Solution:
    def myAtoi(self, s: str) -> int:
        try:
            if s == "": return 0

            s = s.strip(" ")

            front = 0
            end = len(s)-1
            fv = [chr(x) for x in range(48, 58)] + ['+', '-']
            ev = [chr(x) for x in range(48, 58)]

            while s[front] not in fv:
                return 0
            while s[end] not in ev:
                end -= 1
            s = s[front:end+1]

            ch = ''

            idx = 0

            while s[idx] == '+' or s[idx] == '-':
                ch = s[idx] + ch
                idx += 1

            if idx == len(s): return 0

            if idx > 1: return 0

            while idx < len(s) and s[idx] in ev:
                ch = ch + s[idx]
                idx += 1

            ans = int(ch)

            if ans < -2**31: return -2**31
            if ans > 2**31-1 : return 2**31-1
            return ans
        except:
            return 0

s = Solution()

s.myAtoi("     -42")