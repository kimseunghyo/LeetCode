class Solution(object):
    def maximum69Number (self, num):
        for i, n in enumerate(str(num)):
            if n == '6':
                return num + (pow(10, len(str(num)) - 1 - i) * 3)
            
        return num