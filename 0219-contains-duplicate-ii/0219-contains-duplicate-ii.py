class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        dic = {}
        
        for i in range(len(nums)):
            if nums[i] in dic and abs(dic[nums[i]] - i) <= k:
                return True
            
            else:
                dic[nums[i]] = i
                
        return False
            