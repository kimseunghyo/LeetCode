class Solution(object):
    def maxProfit(self, prices):
        sell = prices[0]
        profit = 0
        
        for i in range(len(prices)):
            if prices[i] < sell:
                sell = prices[i]
            else:
                if prices[i] - sell > 0:
                    profit = max(prices[i] - sell, profit)
                    
        return profit
        