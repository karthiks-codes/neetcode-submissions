class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        i1 = {}
        res = -1
        for i, c in enumerate(s):
            if c not in i1:
                i1[c] = i
            else:
                res = max(res, i - i1[c] - 1)

        return res




        