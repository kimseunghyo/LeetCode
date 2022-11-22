class Solution(object):
    def numSquares(self, n):
        dp = [i for i in range(n + 1)]
        
        for i in range(2, n + 1):
            for j in range(1, int(sqrt(n)) + 1):
                dp[i] = min(dp[i], dp[i - (j * j)] + 1)
                
        return dp[n]