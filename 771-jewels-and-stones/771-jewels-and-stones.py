class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        dic = {}
        cnt = 0
        
        for j in jewels:
            dic.setdefault(j, 1)
            
        for s in stones:
            if s in dic:
                cnt += 1
        
        return cnt
        