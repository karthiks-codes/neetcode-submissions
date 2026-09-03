class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        li = [[] for _ in range(n)]
        for u, v in edges:
            li[u].append(v)
            li[v].append(u)

        v = set()
        v.add(0)
        queue = []
        queue.append([0, -1])

        while queue:
            node, p = queue.pop()
            for i in li[node]:
                if i == p:
                    continue
                if i in v:
                    return False
                v.add(i)
                queue.append([i, node])

        return len(v) == n

        



        
        