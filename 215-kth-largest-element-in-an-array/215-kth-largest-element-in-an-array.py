class Solution(object):
    def findKthLargest(self, nums, k):
        n = len(nums)
        nums = sorted(nums, reverse=True)
        
        return nums[k - 1]