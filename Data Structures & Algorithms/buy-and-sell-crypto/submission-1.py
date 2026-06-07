class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
    
        for price in prices:
        # Mettre à jour le prix minimum vu jusqu'à présent
            min_price = min(min_price, price)
        
        # Calculer le profit potentiel si on vend aujourd'hui
            current_profit = price - min_price
        
        # Mettre à jour le profit maximum
            max_profit = max(max_profit, current_profit)
    
        return max_profit

