class Solution(object):
    def uniquePaths(self, m, n):
        def dfs(r, c):
            global memo
          
            if r == m - 1 and c == n - 1:
                return 1
            
            if r > m - 1 or c > n - 1:
                return 0
            
            if (r, c) in memo:
                return memo[(r, c)]
            
            cnt = dfs(r + 1, c) + dfs(r, c + 1)
            memo[(r, c)] = cnt
            
            return cnt
            
        global memo   
        memo = {}
        
        return dfs(0, 0)
        