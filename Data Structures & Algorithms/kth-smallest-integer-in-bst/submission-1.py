# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    result = []
    def inorder_traversal(self, root: Optional[TreeNode], k: int) -> List[int]:
        if not root:
            return []
        if len(self.result) == k:
            return
        
        res = []

        res += self.inorder_traversal(root.left, k)
        res += [root.val]
        res += self.inorder_traversal(root.right, k)
        
        result = res
        return res

        

        

        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = self.inorder_traversal(root, k)

        return res[k - 1]
        





        

        