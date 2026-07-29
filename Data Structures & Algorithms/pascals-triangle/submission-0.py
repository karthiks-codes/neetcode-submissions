class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        matrix = []
        for i in range(numRows):
            ans = [1]
            for j in range(1, i + 1):
                ans.append(math.comb(i, j))
            matrix.append(ans)

        return matrix




        