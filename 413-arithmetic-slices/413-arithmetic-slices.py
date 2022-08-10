class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        cnt = 0
        result = 0
        
        for i in range(2, len(nums)):
            if nums[i - 1] - nums[i - 2] == nums[i] - nums[i - 1]:
                cnt += 1
                result += cnt
                
            else:
                cnt = 0
                
        return result