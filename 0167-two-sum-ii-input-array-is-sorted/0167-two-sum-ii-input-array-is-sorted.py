class Solution(object):
    def twoSum(self, numbers, target):
        p1 = 0
        p2 = len(numbers) - 1
        
        while p1 < p2:
            sum_n = numbers[p1] + numbers[p2]
            
            if sum_n == target:
                return [p1 + 1, p2 + 1]
            
            if sum_n < target:
                p1 += 1
                
            else:
                p2 -= 1
            
        
        