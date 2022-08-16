class Solution(object):
    def romanToInt(self, s):
        value = 0
        
        for i in range(len(s)):
            if s[i] == 'I':
                value += 1
                
            elif s[i] == 'V': 
                if s[i - 1] == 'I' and i > 0:
                    value += 3
                else:
                    value += 5
                
            elif s[i] == 'X': 
                if s[i - 1] == 'I' and i > 0:
                    value += 8
                else:
                    value += 10
                
            elif s[i] == 'L': 
                if s[i - 1] == 'X' and i > 0:
                    value += 30
                else:
                    value += 50
                
            elif s[i] == 'C': 
                if s[i - 1] == 'X' and i > 0:
                    value += 80
                else:
                    value += 100
                
            elif s[i] == 'D': 
                if s[i - 1] == 'C' and i > 0:
                    value += 300
                else:
                    value += 500
                
            elif s[i] == 'M': 
                if s[i - 1] == 'C' and i > 0:
                    value += 800
                else:
                    value += 1000
                    
        return value
                