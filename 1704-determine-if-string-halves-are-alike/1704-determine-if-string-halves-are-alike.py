class Solution(object):
    def halvesAreAlike(self, s):
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
                  
        cnt_a = 0
        cnt_b = 0
        
        len_s = len(s)
        
        for i in range(len_s):
            if s[i] in vowels:
                if i < len_s // 2:
                    cnt_a += 1
                
                else:
                    cnt_b += 1
                    
        return True if cnt_a == cnt_b else False