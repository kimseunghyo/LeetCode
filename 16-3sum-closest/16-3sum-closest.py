class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        
        closest = nums[0] + nums[1] + nums[2]
        len_n = len(nums)
        
        for i in range(len_n - 2):
            j = i + 1
            k = len_n - 1
            
            while j < k:
                sum_n = nums[i] + nums[j] + nums[k]
                
                if sum_n == target:
                    return sum_n
                
                if abs(target - sum_n) < abs(target - closest):
                    closest = sum_n
                
                if sum_n < target:
                    j += 1
                    
                else:
                    k -= 1

                    
        return closest