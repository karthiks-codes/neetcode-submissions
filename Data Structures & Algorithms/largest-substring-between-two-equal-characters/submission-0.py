class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        i1 = {}
        i2 = {}

        for i, c in enumerate(s):
            if c not in i1:
                i1[c] = i
            else:
                i2[c] = i

        res = -1
        for c in i2:
            res = max(res, i2[c] - i1[c] -1)

        return res




        