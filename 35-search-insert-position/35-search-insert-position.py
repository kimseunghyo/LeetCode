class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            middle = (left + right) // 2
            result = middle
            
            if target == nums[middle]:
                return result
                
            elif target < nums[middle]:
                right = middle - 1
                
            else:
                left = middle + 1
                result = left
            
        return result
        