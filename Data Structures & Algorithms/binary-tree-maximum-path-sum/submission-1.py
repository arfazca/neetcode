# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=[root.val]
        def init(root: Optional[TreeNode]):
            if not root: return 0
            leftMax=init(root.left)
            leftMax=max(0,leftMax)
            rightMax=init(root.right)
            rightMax=max(0,rightMax)

            res[0]=max(res[0],leftMax+rightMax+root.val)
            return root.val+max(rightMax,leftMax)
        init(root)
        return res[0]