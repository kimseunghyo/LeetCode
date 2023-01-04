class Solution(object):
    def minimumRounds(self, tasks):
        counter = Counter(tasks)
        res = 0
        
        if 1 in counter.values():
            return - 1
        
        for key, value in counter.items():
            if value % 3 == 0:
                res += value // 3
                
            else:
                if value == 2:
                    res += value // 2
                 
                else:
                    res += (value // 3) + 1 
        
        return res
        