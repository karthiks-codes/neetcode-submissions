"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = {}
        q = []
        q.append(node)
        visited[node] = Node(node.val)
        while q:
            cur = q.pop(0) 
            for n in cur.neighbors:
                if n not in visited:
                    visited[n] = Node(n.val)
                    q.append(n)
                visited[cur].neighbors.append(visited[n])

        return visited[node]


        

        
            

        


        