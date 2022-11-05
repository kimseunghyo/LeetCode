class Solution(object):
    def compress(self, chars):
        comp = ""
        len_c = len(chars)
        
        if len_c == 1:
            return 1
        
        p1 = 0
        p2 = p1 + 1
        
        while p2 <= len_c:
            if p2 == len_c or chars[p1] != chars[p2]:
                comp += chars[p1]
                
                if p2 - p1 > 1:
                    comp += str(p2 - p1)
                
                p1 = p2
                p2 = p1 + 1
                
            else:
                p2 += 1
        
        chars[:] = list(comp)
        
        return len(comp)