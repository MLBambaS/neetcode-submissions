class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            bestDay, curMax = -1, 0
            for j in range(i+1, len(prices)):
                if(prices[j]>curMax):
                    bestDay = j
                    curMax = prices[j]
            profit = max (profit, curMax-prices[i])
        return profit

