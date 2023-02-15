from typing import List
from copy import deepcopy as dc


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numpad = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans: List[str] = []
        for i, v in enumerate(digits):
            if i == 0:
                for j in numpad[int(v)]:
                    ans.append(j)
            else:
                newAns: List[str] = []
                for a in ans:
                    for j in numpad[int(v)]:
                        newAns.append(a + j)
                ans = dc(newAns)
        return ans

s = Solution()

print(s.letterCombinations("2"))