class Solution(object):
    def lengthOfLIS(self, nums):
        dp = [1] * len(nums)
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
                       
        return max(dp)
        
        
        