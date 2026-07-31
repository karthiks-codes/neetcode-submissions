# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = []
        queue.append(root)
        ans = []

        while queue:
            qlen = len(queue)
            level = []
            for _ in range(qlen):
                child = queue.pop(0)
                level.append(child.val)
                if child.left:
                    queue.append(child.left)
                if child.right:
                    queue.append(child.right)

            ans.append(level)

        return ans



            

            

        

        
        