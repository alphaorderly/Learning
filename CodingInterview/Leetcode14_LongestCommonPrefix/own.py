from typing import List


def check(s, index, chr):
    if len(s) <= index or s[index] != chr: return False
    else: return True


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len, reverse=True)
        idx = 0
        ch = ''
        while len(strs[0]) > idx:
            c = strs[0][idx]
            for str in strs:
                if len(str) <= idx or str[idx] != c: return ch
            ch = ch + c
            idx += 1
        return ch

s = Solution();

print(s.longestCommonPrefix(["a"]))