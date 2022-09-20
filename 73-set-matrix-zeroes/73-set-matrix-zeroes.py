class Solution(object):
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        
        first_row = False
        first_col = False
        
        for i in range(n):
            if matrix[0][i] == 0:
                first_row = True
        
        for i in range(m):
            if matrix[i][0] == 0:
                first_col = True
            
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                        
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
                    
        for i in range(1, n):
            if matrix[0][i] == 0:
                for j in range(1, m):
                    matrix[j][i] = 0
                    
        if first_row:
            for i in range(n):
                matrix[0][i] = 0
            
        if first_col:
            for i in range(m):
                matrix[i][0] = 0