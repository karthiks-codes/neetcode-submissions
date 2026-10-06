# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        iMap = {value: index for index, value in enumerate(inorder)}
        preIndex = 0

        def dfs(left, right):
            if left > right:
                return None
            nonlocal preIndex
            treeRoot = TreeNode(preorder[preIndex])
            treeMid = iMap[preorder[preIndex]]
            preIndex += 1
            treeRoot.left = dfs(left, treeMid - 1)
            treeRoot.right = dfs(treeMid + 1, right)

            return treeRoot

        return dfs(0, len(preorder) - 1)
            


        