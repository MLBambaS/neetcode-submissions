# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.indMap = {inorder[i]:i for i in range(len(inorder))}
        self.pre_index = 0
        def build(l: int, r:int) -> Optional[TreeNode]:
            if l > r: 
                return None
            rootVal = preorder[self.pre_index]
            root = TreeNode(rootVal)
            self.pre_index += 1
            root.left = build(l, self.indMap[root.val]-1)
            root.right = build(self.indMap[root.val]+1, r)
            return root
        return build(0, len(inorder)-1)
        