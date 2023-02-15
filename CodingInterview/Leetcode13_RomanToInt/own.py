class Solution:
    def romanToInt(self, s: str) -> int:
        rdict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        nv = s[0]
        number=rdict[nv]
        for i in range(1,len(s)):
            bv = nv
            nv = s[i]
            if(rdict[bv]>=rdict[nv]):
                number += rdict[nv]
            else:
                number += rdict[nv] - 2*rdict[bv]
        return number