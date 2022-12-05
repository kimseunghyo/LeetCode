class Solution(object):
    def removeDuplicates(self, nums):
        p1 = 0
        p2 = 1
        cnt = 0
        
        while p2 < len(nums):
            if nums[p1] == nums[p2]:
                if cnt >= 1:
                    nums.pop(p2)
                    
                else:
                    p2 += 1
                    
                cnt += 1
                
            else:
                p1 = p2
                p2 = p1 + 1
                cnt = 0
                
        return len(nums)