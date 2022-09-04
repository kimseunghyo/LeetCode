class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        
        a = 0
        
        while n >= 1:
            if a == 0 and n == 1:
                return True
            
            a += n % 3
            n = n // 3
            
        return False
        