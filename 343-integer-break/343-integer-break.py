class Solution(object):
    def integerBreak(self, n):
        if n < 4:
            return n - 1
        
        a = n % 3
        b = n // 3
        
        if a == 1:
            return int(math.pow(3, b - 1) * 4)
            
        elif a == 2:
            return int(math.pow(3, b) * 2)
            
        else:
            return int(math.pow(3, b))
            