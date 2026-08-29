class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        tracked = set()

        twice = 0

        for row in grid:
            for col in row:
                if col in tracked:
                    twice = col
                tracked.add(col)
        n = len(grid)
        missing = 0
        for i in range(1, n * n + 1):
            if i not in tracked:
                missing = i

        return [twice, missing]




        


        