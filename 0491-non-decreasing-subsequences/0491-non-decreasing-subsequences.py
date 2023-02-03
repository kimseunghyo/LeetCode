class Solution(object):
    def findSubsequences(self, nums):
        res = []
        
        def dfs(idx, path):
            if len(path) > 1:
                res.append(path)
            
            for i in range(idx, len(nums)):
                if not path or (nums[i] >= path[-1]):
                    dfs(i + 1, path + [nums[i]])
                    
        
        dfs(0, [])
        
        return list(set(map(tuple, res)))
        