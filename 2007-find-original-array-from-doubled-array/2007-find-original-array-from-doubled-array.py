class Solution(object):
    def findOriginalArray(self, changed):
        q = deque([])
        res = []
        
        changed.sort()
        
        for c in changed:
            if q and q[0] * 2 == c:
                res.append(q.popleft())
                
            else:
                q.append(c)
                
        return res if not q else []
                