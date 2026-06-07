class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        # Calcul des produits à gauche
        leftProd = 1
        for i in range(n):
            res[i] = leftProd
            leftProd *= nums[i]
        
        # Calcul des produits à droite et combinaison
        rightProd = 1
        for i in range(n-1, -1, -1):
            res[i] *= rightProd
            rightProd *= nums[i]
        
        return res
