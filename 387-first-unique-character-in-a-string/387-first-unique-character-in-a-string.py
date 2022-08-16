class Solution(object):
    def firstUniqChar(self, s):
        counter = Counter(s)
        
        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i
            
        return -1