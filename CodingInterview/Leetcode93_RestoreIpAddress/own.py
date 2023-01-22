from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def ipChecker(ip: str):
            stripped = ip.split(".")
            if len(stripped) != 4: return False
            for s in stripped:
                if s == '0': continue
                if len(s) == 0 or s[0] == '0' or int(s)>255: return False
            return True

        def combination(n: int):
            comb = list()
            for i in range(1, n):
                for j in range(i+1, n):
                    for k in range(j+1, n):
                        comb.append([i, j, k])
            return comb

        if len(s) <= 3: return []

        comb = combination(len(s))
        ans = list()

        for c in comb:
            composite = s[0:c[0]] + '.' + s[c[0]:c[1]] + '.' + s[c[1]:c[2]] + '.' + s[c[2]:]
            if ipChecker(composite):
                ans.append(composite)

        return ans


s = Solution()

print(s.restoreIpAddresses('25525511135'))