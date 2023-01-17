class Solution:
    def intToRoman(self, num: int) -> str:
        ths = ['', 'M', 'MM', 'MMM']
        hnd = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        ten = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        one = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        a = ''
        for i in range(3, -1, -1):
            if i == 3:
                a = a + ths[num//(10**i)]
            elif i == 2:
                a = a + hnd[(num//(10**i)) % 10] 
            elif i == 1:
                a = a + ten[(num//(10**i)) % 10]
            elif i == 0:
                a = a + one[(num//(10**i)) % 10]
        return a

s = Solution()

print(s.intToRoman(1994))