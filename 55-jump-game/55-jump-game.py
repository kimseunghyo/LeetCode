class Solution(object):
    def canJump(self, nums):
        distance = 0
        i = 0
        
        while i <= distance:
            distance = max(distance, i + nums[i])
                
            if distance >= len(nums) - 1:
                return True
            
            i += 1
            
        return False
        