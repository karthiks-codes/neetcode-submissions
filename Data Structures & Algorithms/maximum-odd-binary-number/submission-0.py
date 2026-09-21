class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        c = s.count('1')
        t = len(s)
        res = ''
        if c == 1:
            for i in range(t - c):
                res += '0'
            res += '1'
            return res

        if c > 1:
            for i in range(c - 1):
                res += '1'
            if t - c >= 1:
                for i in range(t - c):
                    res += '0'
            res += '1'
            return res

