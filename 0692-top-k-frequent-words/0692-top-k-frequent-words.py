class Solution(object):
    def topKFrequent(self, words, k):
        res = []
        
        counter = Counter(words)
        sort_c = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
        
        for key, value in sort_c:
            if len(res) < k:
                res.append(key)
            
        return res
        