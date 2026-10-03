class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])
        pacific = set()
        atlantic = set()

        def PDFS(r, c, prev):
            if (r, c) in pacific or r < 0 or r == row or c < 0 or c == col or prev > heights[r][c]:
                return

            pacific.add((r, c))
            PDFS(r + 1, c, heights[r][c])
            PDFS(r - 1, c, heights[r][c])
            PDFS(r, c + 1, heights[r][c])
            PDFS(r, c - 1, heights[r][c])

        def ADFS(r, c, prev):
            if (r, c) in atlantic or r < 0 or r == row or c < 0 or c == col or prev > heights[r][c]:
                return

            atlantic.add((r, c))
            ADFS(r + 1, c, heights[r][c])
            ADFS(r - 1, c, heights[r][c])
            ADFS(r, c + 1, heights[r][c])
            ADFS(r, c - 1, heights[r][c])

        for r in range(row):
            PDFS(r, 0, heights[r][0])
            ADFS(r, col - 1, heights[r][col - 1])

        for c in range(col):
            PDFS(0, c, heights[0][c])
            ADFS(row - 1, c, heights[row - 1][c])

        res = []
        for i in range(row):
            for j in range(col):
                if (i, j) in pacific and (i, j) in atlantic:
                    res.append([i, j])

        return res

        

        