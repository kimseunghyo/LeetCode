class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        
        else:
            a = 0
            
            while n > 1:
                a += n % 3
                n = n // 3
                
            if a == 0:
                return True
            
            else:
                return False
        