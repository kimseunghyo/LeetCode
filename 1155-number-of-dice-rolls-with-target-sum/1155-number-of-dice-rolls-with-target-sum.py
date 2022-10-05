class Solution(object):
    def numRollsToTarget(self, n, k, target):
        memo = {}
        
        def dfs(sum_n, dice):
            if sum_n == target and dice == n:
                return 1
            
            if sum_n > target or dice > n:
                return 0
            
            if (sum_n, dice) in memo:
                return memo[(sum_n, dice)]
            
            cnt = 0
            
            for i in range(1, k + 1):
                cnt += dfs(sum_n + i, dice + 1)
             
            memo[(sum_n, dice)] = cnt
            
            return cnt
            
            
        return dfs(0, 0) % 1000000007

                
                
        