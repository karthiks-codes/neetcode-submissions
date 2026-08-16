# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 == None and root2 == None:
            return True
        elif root1 != None and root2 != None and root1.val == root2.val:
            return self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right)
        else:
            return False



    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = []
        stack.append(root)

        while stack:
            newRoot = stack.pop()
            if self.isSameTree(newRoot, subRoot):
                return True
            if newRoot:
                stack.append(newRoot.left)
                stack.append(newRoot.right)

        return False
            
        

        