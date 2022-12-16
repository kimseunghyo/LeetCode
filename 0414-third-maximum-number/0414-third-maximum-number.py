class Solution(object):
    def thirdMax(self, nums):        
        sort_n = sorted(list(set(nums)), reverse=True)
        
        if len(sort_n) < 3:
            return sort_n[0]
        
        else:
            return sort_n[2]