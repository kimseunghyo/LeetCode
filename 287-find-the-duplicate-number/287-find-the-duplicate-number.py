import collections

class Solution(object):
    def findDuplicate(self, nums):
        return (Counter(nums).most_common())[0][0]