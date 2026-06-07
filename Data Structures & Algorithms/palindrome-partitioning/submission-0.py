class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def is_palindrome(sub_str):
            return sub_str == sub_str[::-1]
        
        def backtracking(start, current):
            # Si nous avons atteint la fin de la chaîne, nous avons une partition valide
            if start == len(s):
                res.append(current[:])
                return
            
            # Essayer toutes les sous-chaînes possibles à partir de la position actuelle
            for i in range(start, len(s)):
                # Extraire la sous-chaîne de start à i (inclus)
                sub_str = s[start:i+1]
                
                # Vérifier si la sous-chaîne est un palindrome
                if is_palindrome(sub_str):
                    # Ajouter cette sous-chaîne à la partition actuelle
                    current.append(sub_str)
                    
                    # Récursivement traiter le reste de la chaîne
                    backtracking(i+1, current)
                    
                    # Backtrack: retirer la dernière sous-chaîne
                    current.pop()
        
        backtracking(0, [])
        return res