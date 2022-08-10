class Solution(object):
    def rob(self, nums):
        dp = [0] * len(nums)
        
        dp = [n for n in nums]
        
        for i in range(1, len(nums)):
            if i == 1:
                dp[i] = max(dp[i - 1], dp[i])
            else:
                dp[i] = max(dp[i - 1], dp[i - 2] +dp[i])
            
        return dp[-1]
        