# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def init(root: Optional[TreeNode], level: int, mainList: List[int]):
            if not root:
                return mainList
            if len(mainList)==level:
                mainList.append(root.val)
            init(root.right, level+1, mainList)
            init(root.left, level+1, mainList)
            return mainList
        return init(root, 0, [])