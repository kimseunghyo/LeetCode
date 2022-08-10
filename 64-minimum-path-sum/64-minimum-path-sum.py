class Solution(object):
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                    continue
                    
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                    
                else:
                    dp[i][j] = min(grid[i][j] + dp[i - 1][j], grid[i][j] + dp[i][j - 1])
                    
        return dp[m - 1][n - 1]