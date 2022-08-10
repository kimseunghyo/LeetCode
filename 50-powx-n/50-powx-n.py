class Solution(object):
    def myPow(self, x, n):
        def pow(x, n):
            if x == 1 or n == 0:
                return 1
            
            elif n == 1:
                return x
            
            if n < 0:
                return pow(1 / x, -n)
            
            else:
                xn = pow(x, n // 2)

                if n % 2 == 0:
                    return xn * xn

                else:
                    return x * xn * xn
            
        return pow(x, n)
                
        