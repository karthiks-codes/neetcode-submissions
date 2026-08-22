# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        res = self.inOrder(root.left)
        res += [root.val]
        res += self.inOrder(root.right)

        return res
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = self.inOrder(root)
        j = len(res)

        sum = 0
        for k in range(j):
            if res[k] >= low and res[k] <= high:
                sum += res[k]

            if k + 1 < j and res[k + 1] > high:
                break

        

        return sum
        
        