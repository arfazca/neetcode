"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        OldToNew = {}

        def init (root: Optional['Node']):
            if root in OldToNew: return OldToNew[root]

            NewRoot = Node(root.val)
            OldToNew[root]=NewRoot

            for neighbors in root.neighbors:
                NewRoot.neighbors.append(init(neighbors))
            return NewRoot

        return init(node) if node else None