# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
            if not tree1 and not tree2: return True
            if not tree1 or not tree2: return False
            if tree1.val != tree2.val: return False
            return isSameTree(tree1.left, tree2.left) and isSameTree(tree1.right, tree2.right)
        if isSameTree(root, subRoot):
            return True
        if root.left and self.isSubtree(root.left, subRoot) or root.right and self.isSubtree(root.right, subRoot):
            return True
        return False
        