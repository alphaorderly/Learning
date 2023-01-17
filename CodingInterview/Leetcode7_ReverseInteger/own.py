class Solution:
    def reverse(self, x: int) -> int:
        if x == 0: return 0

        xs = 'x' + str(x)
        xs = xs[::-1].strip('0')
        xs = xs[:len(xs)-1]
        if xs[len(xs)-1] == '-':
            ans = int('-' + xs[:len(xs)-1])
        else:
            ans = int(xs[:len(xs)])

        if -2**31 > ans or ans > 2**31-1: return 0
        else: return ans

s = Solution()

print(s.reverse(0))