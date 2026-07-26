class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r = len(matrix)
        c = len(matrix[0])

        res = [row.copy() for row in matrix]
        print(res)

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    for cols in range(c):
                        
                        res[i][cols] = 0
                    for rows in range(r):
                        
                        res[rows][j] = 0


        for i in range(r):
            for j in range(c):
                matrix[i][j] = res[i][j]
        
        