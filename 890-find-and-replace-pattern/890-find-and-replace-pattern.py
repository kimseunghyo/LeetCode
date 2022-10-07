class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        if len(pattern) == 1:
            return words
        
        res = []
        
        for w in words:
            dic = {}
            temp = True
            
            for i in range(len(w)):
                if dic.setdefault(pattern[i], w[i]) != w[i]:
                    temp = False
                    
            if temp and len(set(dic.values())) == len(dic):
                res.append(w)
                     
        return res
            
        