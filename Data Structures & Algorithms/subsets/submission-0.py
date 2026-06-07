class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(start, current):
            # Ajouter le sous-ensemble actuel au résultat
            result.append(current[:])
        
            # Explorer tous les candidats possibles
            for i in range(start, len(nums)):
                # Inclure nums[i] dans le sous-ensemble actuel
                current.append(nums[i])
            
                # Explorer plus loin avec cet élément inclus
                backtrack(i + 1, current)
            
                # Exclure nums[i] pour explorer d'autres possibilités (backtrack)
                current.pop()
    
        backtrack(0, [])
        return result




        