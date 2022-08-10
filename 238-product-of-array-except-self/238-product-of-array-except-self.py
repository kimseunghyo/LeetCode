class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        
        answer = [0] * n
        left = [1] * n
        right = [1] * n
        
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
            right[i] = right[i - 1] * nums[n - i]
            
        for i in range(n):
            answer[i] = left[i] * right[n - 1 - i]
            
        return answer
        