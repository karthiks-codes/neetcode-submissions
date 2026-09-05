class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adjList = defaultdict(set)

        def dfs(vertex):
            for i in adjList[vertex]:
                if i not in visited:
                    visited.add(i)
                    dfs(i)

        res = 0
        for u,v in edges:
            adjList[u].add(v)
            adjList[v].add(u)

        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                res += 1
            
        return res

        

            


        

        
        

        