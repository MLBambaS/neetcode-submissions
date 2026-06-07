# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder: 
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        rootVal = preorder[0]
        index = inorder.index(rootVal)
        root = TreeNode(rootVal)
        root.left = self.buildTree(preorder[1:1+index], inorder[:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return root
        