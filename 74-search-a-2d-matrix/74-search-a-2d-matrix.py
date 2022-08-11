class Solution(object):
    def searchMatrix(self, matrix, target):        
        r = 0
        c = len(matrix[0]) - 1
        
        while r < len(matrix) and c >= 0:
            if matrix[r][c] == target:
                return True
            
            elif matrix[r][c] < target:
                r += 1
                
            else:
                c -= 1
                
        return False
        