class Solution(object):
    def romanToInt(self, s):
        dict_s = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        integer = 0
        
        for i in range(len(s)):
            if dict_s[s[i - 1]] < dict_s[s[i]] and i > 0:
                integer += dict_s[s[i]] - dict_s[s[i - 1]] * 2
            
            else:
                integer += dict_s[s[i]]
                    
        return integer
                