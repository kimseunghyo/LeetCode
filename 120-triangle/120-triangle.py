class Solution(object):
    def minimumTotal(self, triangle):
        dp = triangle
        
        for i in range(1, len(triangle)):
            n = len(triangle[i])
            
            for j in range(n):
                if j == 0:
                    dp[i][j] += dp[i - 1][j] 
                
                elif j == n - 1:
                    dp[i][j] += dp[i - 1][j - 1]
                    
                else:
                    dp[i][j] += min(dp[i - 1][j - 1], dp[i - 1][j])
                    
        return min(dp[-1])
        