class Solution:
    def minOperations(self, s: str) -> int:
        res1 = 0
        res2 = 0
        c1 = 0
        c2 = 1

        for i in s:
            if int(i) != c1:
                res1 += 1
            elif int(i) != c2:
                res2 += 1
            c1 ^= 1
            c2 ^= 2

        return min(res1, res2)


        