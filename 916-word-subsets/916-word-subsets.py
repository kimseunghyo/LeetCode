class Solution(object):
    def wordSubsets(self, words1, words2):
        res = []
        subsets = defaultdict(int)
        
        for w2 in words2:
            cnt_w2 = Counter(w2)
            
            for key in cnt_w2:
                subsets[key] = max(subsets[key], cnt_w2[key])
                
        for w1 in words1:
            cnt_w1 = Counter(w1)
            temp = True
            
            for key in subsets:
                if cnt_w1[key] < subsets[key]:
                    temp = False
                    
                    break
                    
            if temp:
                res.append(w1)
            
        return res