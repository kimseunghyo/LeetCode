class Solution(object):
    def minSetSize(self, arr):
        counter = Counter(arr)
        values = sorted(counter.values(), reverse=True)
        
        n = len(arr) // 2
        min_size = 0
        
        for v in values:
            n -= v
            min_size += 1
            
            if n <= 0:
                return min_size

        