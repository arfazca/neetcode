# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ggXX = 0
        def dXX(root:TreeNode):
            if not root: return 0
            left = dXX(root.left)
            right = dXX(root.right)
            self.ggXX = max(self.ggXX,left+right)
            return 1+max(left,right)
        dXX(root)
        return self.ggXX