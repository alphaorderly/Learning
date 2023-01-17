def validPalindrome(s: str):
    for i in range(0, len(s)//2):
        if s[i] != s[len(s)-1-i]: return False
    return True

class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(1, len(s)):
            for j in range(i):
                if s[j] == s[j+len(s)-i] and validPalindrome(s[j:j+len(s)-i+1]):
                    return s[j:j+len(s)-i+1]
        return s[0]
