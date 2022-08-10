class Solution(object):
    def findTargetSumWays(self, nums, target): 
        def dfs(idx, sum_n):
            global memo
            
            if idx == len(nums):
                if sum_n == target:
                    return 1
                else:
                    return 0
                
            if (idx, sum_n) in memo:
                return memo[(idx, sum_n)]
            
            cnt = dfs(idx + 1, sum_n + nums[idx]) + dfs(idx + 1, sum_n - nums[idx])
        
            memo[(idx, sum_n)] = cnt
        
            return cnt
        
        global memo
        memo = {}
        return dfs(0, 0)