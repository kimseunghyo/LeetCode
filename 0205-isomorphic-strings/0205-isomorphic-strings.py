class Solution(object):
    def isIsomorphic(self, s, t):
        dic = {}
        
        for i in range(len(s)):
            if s[i] not in dic and t[i] in dic.values():
                return False
            
            if dic.setdefault(s[i], t[i]) != t[i]:
                return False
            
        return True