class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cmap = defaultdict(list)
        for i, j in prerequisites:
            cmap[i].append(j)

        visited = set()

        def dfs(node):
            if node in visited:
                return False
            if not cmap[node]:
                return True

            visited.add(node)
            for i in cmap[node]:
                if dfs(i) == False:
                    return False
            visited.remove(node)
            cmap[node] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True



        