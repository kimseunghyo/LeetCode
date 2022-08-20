class Solution(object):
    def combinationSum2(self, candidates, target):
        def dfs(target, idx, path):
            if target == 0:
                result.append(path)
                
            if target < 0:
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                    
                dfs(target - candidates[i], i + 1, path + [candidates[i]])
                
        
        result = []
        candidates.sort()
        
        dfs(target, 0, [])
            
        return result