# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, node: TreeNode, maxValue) -> int:
        if not node:
            return 0
        
        count = 1 if node.val >= maxValue else 0
        
        if node.left:
            count += self.traverse(node.left, max(maxValue, node.val))
        if node.right:
            count += self.traverse(node.right, max(maxValue, node.val))
        
        return count

    def goodNodes(self, root: TreeNode) -> int:
        count = 1
        if root.left:
            count += self.traverse(root.left, root.val)
        if root.right:
            count += self.traverse(root.right, root.val)

        return count
            
        