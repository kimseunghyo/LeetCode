class Solution(object):
    def combinationSum3(self, k, n):
        res = []
        
        def dfs(idx, sum_n, path):
            if len(path) == k and sum_n == n:
                res.append(path)
                
            if len(path) > k or sum_n > n:
                return
            
            for i in range(idx, 10):
                dfs(i + 1, sum_n + i, path + [i])
            
        
        dfs(1, 0, [])
        
        return res
        