class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        
        def dfs(target, start, path):
            if target == 0:
                result.append(path)
                
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                dfs(target - candidates[i], i, path + [candidates[i]])
            
            
        dfs(target, 0, path = [])
        
        return result
            
        