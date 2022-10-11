class Solution(object):
    def increasingTriplet(self, nums):
        len_n = len(nums)
        
        if len(set(nums)) < 3:
            return False
        
        for i in range(len_n - 2):
            j = i + 1
            k = len_n - 1
            
            while j < k:
                if nums[i] < nums[j] < nums[k]:
                    return True
                
                if nums[i] >= nums[j] or (nums[i] < nums[j + 1] and nums[j] >= nums[j + 1]):
                    j += 1

                if nums[j] >= nums[k]:
                    k -= 1
                
                
        return False