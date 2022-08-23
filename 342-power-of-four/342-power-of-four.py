class Solution(object):
    def isPowerOfFour(self, n):
        if n <= 0:
            return False
        
        else:
            a = 0
            
            while n > 1:
                a += n % 4
                n = n // 4
                
            if a == 0:
                return True
            
            else:
                return False