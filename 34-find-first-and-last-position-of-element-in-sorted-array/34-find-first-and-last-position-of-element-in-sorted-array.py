class Solution(object):
    def searchRange(self, nums, target):
        left = 0
        right = len(nums) - 1
        
        fpos = -1
        lpos = -1
        
        while left <= right:
            middle = (left + right) // 2
            
            if nums[middle] == target:
                fpos = middle
                lpos = middle
                
                break
            
            elif nums[middle] > target:
                right = middle - 1
                
            else:
                left = middle + 1
        
        
        if fpos != -1:
            for i in range(middle):
                if nums[middle -1 - i] == target:
                    fpos = middle -1 - i
                else:
                    break
            
            for i in range(middle + 1, len(nums)):
                if nums[i] == target:
                    lpos = i
                else:
                    break
                
        return [fpos, lpos]