def validPalindrome(s: str):
    for i in range(0, len(s)//2):
        if s[i] != s[len(s)-1-i]: return False
    return True

class Solution:
    def longestPalindrome(self, s: str) -> str:
        lst = list()
        for i in range(len(s)):
            for j in range(i, len(s)):
                newstr = s[i:j+1]
                if validPalindrome(newstr): lst.append(newstr)
        lst.sort(key=len, reverse=True)
        return lst[0]

