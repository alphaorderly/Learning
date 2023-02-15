from functools import cmp_to_key
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        characterOrder = dict()
        i = 0
        for ch in order:
            characterOrder[ch] = i
            i += 1
        def compare(a, b):
            for i in range(len(a) if len(a) < len(b) else len(b)):
                if a[i] != b[i]:
                    return characterOrder[a[i]] - characterOrder[b[i]]
            return len(a) - len(b)
        std = sorted(words, key=cmp_to_key(compare))
        
        if len(std) != len(words): return False
        for i in range(len(std)):
            if std[i] != words[i]: return False
        return True
        

s = Solution()

print(s.isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz"))