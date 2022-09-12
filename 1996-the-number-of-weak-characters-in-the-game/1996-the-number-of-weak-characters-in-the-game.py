class Solution(object):
    def numberOfWeakCharacters(self, properties):
        properties.sort(key=lambda x:(-x[0], x[1]))
        defense = properties[0][1]
        cnt = 0
        
        for i in range(len(properties)):
            if properties[i][1] < defense:
                cnt += 1
            
            else:
                defense = properties[i][1]
                
        return cnt
            
        