class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [k for k in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(u):
            if u != parent[u]:
                parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            p1, p2 = find(u), find(v)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                parent[p2] = parent[p1]
                rank[p1] += rank[p2]
            else:
                parent[p1] = parent[p2]
                rank[p2] += rank[p1]
            return True

        for u, v in edges:
            p = union(u, v)
            if not p:
                return [u, v]

        
        

        
        