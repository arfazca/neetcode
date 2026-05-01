# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        out = []
        def init(root: Optional[TreeNode]):
            if not root: 
                out.append("N")
                return
            out.append(str(root.val))
            init(root.left)
            init(root.right)
        init(root)
        return ",".join(out)
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.i = 0
        V = data.split(",")
        def init():
            if V[self.i]=="N":
                self.i+=1
                return None
            node = TreeNode(V[self.i])
            self.i+=1
            node.left = init()
            node.right = init()
            return node
        return init()