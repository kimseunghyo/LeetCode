class Solution(object):
    def moveZeroes(self, nums):
        for i in range(len(nums)):
            if nums[i] == 0:
                for j in range(i + 1, len(nums)):
                    if nums[j] == 0:
                        continue
                    else:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                    
                
                