class Solution(object):
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1
        
        while left < right:
            if nums[left] <= nums[right]:
                return nums[left]
            
            middle = (left + right) // 2
            
            if nums[left] <= nums[middle]:
                left = middle + 1
                
            else:
                right = middle
                
        return nums[left]
                
        