class Solution(object):
    def findLonely(self, nums):
        count = Counter(nums)
        res = []
        
        for n in nums:
            if count[n] == 1 and (n - 1 not in count) and (n + 1 not in count):
                res.append(n)
                
        return res