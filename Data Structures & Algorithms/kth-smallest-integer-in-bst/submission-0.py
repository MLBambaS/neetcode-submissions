# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def addInOrder(node):
            nonlocal res
            if not node:
                return
            if node.left:
                addInOrder(node.left)
                if len(res) == k: return res[k-1]
            res.append(node.val)
            if len(res) == k: return node.val
            if node.right:
                addInOrder(node.right)
                if len(res) == k: return res[k-1]
        return addInOrder(root)