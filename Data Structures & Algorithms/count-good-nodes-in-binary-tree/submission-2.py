# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(node: TreeNode, maxInWay: int):
            if not node: return
            if maxInWay <= node.val:
                self.count+=1
                maxInWay = node.val
            dfs(node.left, maxInWay)
            dfs(node.right, maxInWay)
        dfs(root, float('-inf'))
        return self.count

        