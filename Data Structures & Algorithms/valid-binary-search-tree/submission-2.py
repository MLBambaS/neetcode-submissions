# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
        
            if node.val <= lower or node.val >= upper:
                return False
        
            # Vérifier le sous-arbre gauche avec une limite supérieure mise à jour
            # Tous les nœuds du sous-arbre gauche doivent être < node.val
            if not validate(node.left, lower, node.val):
                return False
        
            # Vérifier le sous-arbre droit avec une limite inférieure mise à jour
            # Tous les nœuds du sous-arbre droit doivent être > node.val
            if not validate(node.right, node.val, upper):
                return False
        
            return True
    
        return validate(root)
        