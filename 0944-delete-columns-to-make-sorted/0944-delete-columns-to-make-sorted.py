class Solution(object):
    def minDeletionSize(self, strs):
        res = 0
        
        for col in range(len(strs[0])):
            for row in range(1, len(strs)):
                if strs[row][col] < strs[row - 1][col]:
                    res += 1
                    
                    break
                
        return res