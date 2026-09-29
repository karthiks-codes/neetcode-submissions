class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        row = len(grid)
        col = len(grid[0])
        visited = set()
        fresh = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    visited.add((i, j))

                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        
        def helper(r, c):
            if r < 0 or r == row or c < 0 or c == col or grid[r][c] == 0 or (r, c) in visited:
                return
            
            nonlocal fresh
            visited.add((r, c))
            if grid[r][c] == 1:
                grid[r][c] = 2
                fresh -= 1
            queue.append((r, c))


        count = -1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.pop(0)
                visited.add((r, c))
                helper(r + 1, c)
                helper(r - 1, c)
                helper(r, c + 1)
                helper(r, c - 1)

            count += 1

        if fresh > 0:
            return -1
        return count



        

                



        