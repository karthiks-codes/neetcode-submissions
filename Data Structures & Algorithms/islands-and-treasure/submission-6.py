class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        queue = []
        visited = set()

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))

        def visitRoom(r, c):
            if r < 0 or r == row or c < 0 or c == col or (r, c) in visited or grid[r][c] == -1:
                return
            queue.append((r, c))
            visited.add((r, c))

        dist = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.pop(0)
                grid[r][c] = dist
                visitRoom(r + 1, c)
                visitRoom(r - 1, c)
                visitRoom(r, c + 1)
                visitRoom(r, c - 1)
                
            dist += 1

                



        