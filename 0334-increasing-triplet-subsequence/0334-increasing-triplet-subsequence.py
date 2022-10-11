class Solution(object):
    def increasingTriplet(self, nums):
        len_n = len(nums)
        
        if len_n < 3:
            return
        
        first = float("inf")
        second = float("inf")
        
        for n in nums:
            if n <= first:
                first = n
                
            elif n <= second:
                second = n
                
            else:
                return True
                
        return False