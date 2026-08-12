"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
    
        nodeDict = {}
        cur = head

        while cur:
            new = Node(cur.val, None, None)
            nodeDict[cur] = new
            cur = cur.next

        cur = head

        while cur:
            new = nodeDict[cur]
            new.next = nodeDict[cur.next] if cur.next else None
            new.random = nodeDict[cur.random] if cur.random else None
            cur = cur.next


        return nodeDict[head]



        