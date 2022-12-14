class Solution(object):
    def arrayNesting(self, nums):
        s = set()
        self.res = 0
        
        def dfs(i, cnt):
            if i in s:
                return
            
            s.add(i)
            self.res = max(self.res, cnt)
            
            return dfs(nums[i], cnt + 1)
            
        
        for i in range(len(nums)):
            if i not in s:
                dfs(i, 1)
            
        return self.res
        