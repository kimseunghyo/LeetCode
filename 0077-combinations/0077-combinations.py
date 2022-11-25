class Solution(object):
    def combine(self, n, k):
        res = []
        
        def dfs(idx, path):
            if len(path) == k:
                res.append(path)
                
            for i in range(idx, n + 1):
                dfs(i + 1, path + [i])
            
        
        for i in range(1, n + 1):
            dfs(i + 1, [i])
            
        return res