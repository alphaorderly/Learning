class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i <= j:
            if s[i] != s[j]:
                break
            i += 1
            j -= 1
        if i > j: 
            return True

        # 오른쪽에 1개 지우기
        i = 0
        j = len(s)-1
        once = False
        while i <= j:
            if s[i] != s[j] and not once:
                j -= 1
                once = True
                continue
            elif s[i] != s[j]:
                break
            i += 1
            j -= 1
        if i > j: 
            return True

        # 왼쪽에 1개 지우기
        i = 0
        j = len(s)-1
        once = False
        while i <= j:
            if s[i] != s[j] and not once:
                i += 1
                once = True
                continue
            elif s[i] != s[j]:
                break
            i += 1
            j -= 1
        if i > j: 
            return True

        return False
