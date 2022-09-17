class Solution(object):
    def maximumScore(self, nums, multipliers):
        n = len(nums)
        m = len(multipliers)
        dp = [[0] * (m + 1) for _ in range(m + 1)] 
        
        for i in range(m - 1, -1, -1):
            for j in range(i, -1, -1):
                start = nums[j] * multipliers[i] +dp[i + 1][j + 1]
                end = nums[n - 1 - (i - j)] * multipliers[i] + dp[i + 1][j]
                
                dp[i][j] = max(start, end) 
                
        return dp[0][0]