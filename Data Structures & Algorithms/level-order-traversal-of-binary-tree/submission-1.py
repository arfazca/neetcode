# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def init(root: Optional[TreeNode], level: int, mainList: List[List[int]]) -> List[List[int]]:
            if not root:
                return mainList
            if len(mainList) == level:
                mainList.append([])
            mainList[level].append(root.val)
            if root.left:
                init(root.left, level+1, mainList)
            if root.right:
                init(root.right, level+1, mainList)
            return mainList
        return init(root, 0, [])