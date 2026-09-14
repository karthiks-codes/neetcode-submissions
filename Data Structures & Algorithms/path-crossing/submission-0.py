class Solution:
    def isPathCrossing(self, path: str) -> bool:
        current = (0, 0)
        visited = defaultdict(int)
        visited[current] += 1
        for i in path:
            if i == 'N':
                current = (current[0], current[1] + 1)
            elif i == 'S':
                current = (current[0], current[1] - 1)
            elif i == 'E':
                current = (current[0] + 1, current[1])
            elif i == 'W':
                current = (current[0] - 1, current[1])

            visited[current] += 1
            if visited[current] > 1:
                return True

        return False

        

            

        

        

        