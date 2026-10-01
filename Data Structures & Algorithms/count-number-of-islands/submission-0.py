class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = set()
        noOfIslands = 0

        def BFS(r, c):
            queue = [(r, c)]
            visited.add((r, c))
            while queue:
                r, c = queue.pop(0)
                if r in range(row) and c + 1 in range(col):
                    if grid[r][c + 1] == '1' and (r, c + 1) not in visited:
                        visited.add((r, c + 1))
                        queue.append((r, c + 1))
                if r in range(row) and c - 1 in range(col):
                    if grid[r][c - 1] == '1' and (r, c - 1) not in visited:
                        visited.add((r, c - 1))
                        queue.append((r, c - 1))
                if r + 1 in range(row) and c in range(col):
                    if grid[r + 1][c] == '1' and (r + 1, c) not in visited:
                        visited.add((r + 1, c))
                        queue.append((r + 1, c))
                if r - 1 in range(row) and c in range(col):
                    if grid[r - 1][c] == '1' and (r - 1, c) not in visited:
                        visited.add((r - 1,c))
                        queue.append((r - 1, c))
    
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r, c) not in visited:
                    BFS(r, c)
                    noOfIslands += 1

        return noOfIslands
        
        