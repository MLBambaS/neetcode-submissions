class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float("inf")
        profit = 0
        for p in prices:
                minPrice = min(minPrice, p)
                profit = max(p-minPrice, profit)
        return profit