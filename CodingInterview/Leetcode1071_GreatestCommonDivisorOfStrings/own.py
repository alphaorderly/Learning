class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def divider(dividened: str, divider: str):
            if divider == '': return True

            while len(dividened) >= len(divider):
                if not dividened.startswith(divider): return False
                dividened = dividened[len(divider):]

            if len(dividened) == 0: return True
            else: return False

        short = str1 if len(str1) < len(str2) else str2

        chr = ''

        index = 0

        ans = ''

        while True:
            if divider(str1, chr) and divider(str2, chr):
                ans = chr
            if index == len(short): break
            chr = chr + short[index]
            index += 1

        return ans