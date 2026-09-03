class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        adjList = [[] for _ in range(n)]

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        visited = set()
        visited.add(0)
        stack = []
        stack.append([0, -1])

        while stack:
            node, parent = stack.pop()
            for i in adjList[node]:
                if i == parent:
                    continue
                if i in visited:
                    return False
                visited.add(i)
                stack.append([i, node])

        return len(visited) == n



        
        