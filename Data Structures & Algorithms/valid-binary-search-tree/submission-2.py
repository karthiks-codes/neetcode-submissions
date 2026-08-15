# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inOrderTraversal(self, root: Optional[TreeNode]) -> list:
        if not root:
            return []
        
        res = self.inOrderTraversal(root.left)
        res += [root.val]
        res += self.inOrderTraversal(root.right)

        return res

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        traverse = self.inOrderTraversal(root)

        for i in range(1, len(traverse)):
            if traverse[i] <= traverse[i - 1]:
                return False

        return True


        
        