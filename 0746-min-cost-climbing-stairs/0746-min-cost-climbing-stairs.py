class Solution(object):
    def minCostClimbingStairs(self, cost):
        dp = cost
        n = len(cost)
        
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
            
        return min(dp[n - 1], dp[n - 2])