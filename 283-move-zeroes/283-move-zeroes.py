class Solution(object):
    def moveZeroes(self, nums):
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.append(nums[i])
                nums.remove(nums[i])
                
                