class Solution(object):
    def maxIceCream(self, costs, coins):
        sort_c = sorted(costs)
        cnt = 0
        
        for c in sort_c:
            if c <= coins:
                coins -= c
                cnt += 1
                
        return cnt
        