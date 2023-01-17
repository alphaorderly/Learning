from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [set() for _ in range(n+1)]
        dp[1].add("()")

        for i in range(2, n+1):
            for v in dp[i-1]:
                dp[i].add("()" + v)
                dp[i].add(v + "()")
                dp[i].add("("+v+")")
            for k in range(1, i):
                for p in range(1, i):
                    if k + p != i: continue
                    kv = dp[k]
                    pv = dp[p]
                    for kvs in kv:
                        for pvs in pv:
                            dp[i].add(kvs + pvs)
                            dp[i].add(pvs +  kvs)
        return list(dp[n])

s = Solution()

print(s.generateParenthesis(5))