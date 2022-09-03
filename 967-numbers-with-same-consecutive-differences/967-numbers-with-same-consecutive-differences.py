class Solution(object):
    def numsSameConsecDiff(self, n, k):
        result = []
        
        def dfs(x, path):
            if len(str(path)) == n:
                result.append(path)
                
                return
            
            for i in range(10):
                if abs(i - x) == k:
                    dfs(i, str(path) + str(i))

                    
        for i in range(1, 10):
            dfs(i, i)
        
        return result