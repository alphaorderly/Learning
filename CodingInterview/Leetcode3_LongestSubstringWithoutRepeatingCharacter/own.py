class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 저장용 변수
        if len(s) == 0: return 0
        checker = dict()
        start = 0
        cnt = [0 for x in range(len(s))]
        for i in range(len(s)):
            # 중복이 아닐때
            if s[i] not in checker:
                checker[s[i]] = i
                if i == 0:
                    cnt[i] = 1
                else:
                    cnt[i] = cnt[i-1] + 1
            else:
                # 중복이지만 문자열에 포함은 안될때
                if checker[s[i]] < start:
                    checker[s[i]] = i
                    cnt[i] = cnt[i-1] + 1
                # 중복이면서 문자열에 포함될때
                else:
                    cnt[i] = i - checker[s[i]]
                    start = checker[s[i]] + 1
                    checker[s[i]] = i
        return max(cnt)
                


s = Solution()

print(s.lengthOfLongestSubstring(""))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))