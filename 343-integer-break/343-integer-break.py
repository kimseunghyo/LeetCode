class Solution(object):
    def integerBreak(self, n):
        if n < 4:
            return n - 1
        
        a = n // 3
        b = n % 3
        
        if b == 1:
            return int(math.pow(3, a - 1) * 4)
            
        elif b == 2:
            return int(math.pow(3, a) * 2)
            
        else:
            return int(math.pow(3, a))
            