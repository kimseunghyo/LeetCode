class Solution(object):
    def minSteps(self, s, t):
        counter1 = Counter(s)
        counter2 = Counter(t)        
        
        def anagram(cnt1, cnt2):
            cnt = 0
        
            for key, value in cnt1.items():
                if key not in cnt2:
                    cnt += cnt1[key]
                    
                else:
                    if cnt1[key] < cnt2[key]:
                        cnt += cnt2[key] - cnt1[key]
                    
            return cnt
        

        return anagram(counter1, counter2) + anagram(counter2, counter1)