# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        res = []

        res += self.inorder_traversal(root.left)
        res += [root.val]
        res += self.inorder_traversal(root.right)
        

        return res

        

        

        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = self.inorder_traversal(root)

        return res[k - 1]
        





        

        