class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort(reverse=True)
        perimeter = 0
        
        for i in range(len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                perimeter = max(perimeter, nums[i] + nums[i + 1] + nums[i + 2])

        return perimeter
        