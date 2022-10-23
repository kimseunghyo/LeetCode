class Solution(object):
    def findErrorNums(self, nums):
        counter = Counter(nums)
        
        for i in range(1, len(nums) + 1):
            if counter[i] == 2:
                twice_n = i
            
            if i not in counter:
                miss_n = i
        
        return [twice_n, miss_n]