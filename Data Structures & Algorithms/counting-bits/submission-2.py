class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            i = bin(i)[2:]
            res.append(i.count('1'))

        return res

        