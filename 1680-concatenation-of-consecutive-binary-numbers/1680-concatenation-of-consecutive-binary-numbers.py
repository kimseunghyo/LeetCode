class Solution(object):
    def concatenatedBinary(self, n):
        bin_n = ""
        
        for i in range(n + 1):
            b = format(i, 'b')
            bin_n += b
            
        dec_n = int(str(bin_n), 2)
        
        def pow(x, y):
            if y == 1:
                return x
            
            else:
                xy = pow(x, y // 2)
                
                if y % 2 == 0:
                    return xy * xy
                
                else:
                    return x * xy * xy
        
        return dec_n % (pow(10, 9) + 7)
        