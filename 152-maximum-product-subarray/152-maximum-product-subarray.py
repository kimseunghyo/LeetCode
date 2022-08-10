class Solution(object):
    def maxProduct(self, nums):
        max_dp = [0] * len(nums)
        min_dp  =[0] * len(nums)
        
        max_dp[0] = nums[0]
        min_dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            max_dp[i] = max(nums[i], max_dp[i - 1] * nums[i], min_dp[i - 1] * nums[i])
            min_dp[i] = min(nums[i], max_dp[i - 1] * nums[i], min_dp[i - 1] * nums[i])
            
        return max(max_dp)