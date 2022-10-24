class Solution(object):
    def maxLength(self, arr):
        self.s = 0
        
        def dfs(idx, path):
            if len(path) == len(set(path)):
                self.s = max(self.s, len(path))
                
            for i in range(idx, len(arr)):
                dfs(i + 1, path + arr[i])
                
            
        dfs(0, "")
        
        return self.s