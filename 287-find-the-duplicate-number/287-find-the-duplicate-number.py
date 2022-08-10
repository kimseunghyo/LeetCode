import collections

class Solution(object):
    def findDuplicate(self, nums):
        cnt = collections.Counter(nums)
        
        for key, val in cnt.items():
            if val != 1:
                return key