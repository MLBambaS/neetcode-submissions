# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: return "null"
        return str(root.val)+','+self.serialize(root.left)+','+self.serialize(root.right)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        def dfs(nodes):
            val = nodes.pop(0)
            if val == "null":
                return None
            root = TreeNode(int(val))
            root.left=dfs(nodes)
            root.right=dfs(nodes)
            return root
        nodes = data.split(',')
        return dfs(nodes)