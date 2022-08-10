class Solution(object):
    def rotate(self, matrix):
        def transpose(matrix):
            for i in range(n):
                for j in range(i + 1, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        def reflcet(matrix):
            for i in range(n):
                for j in range(n // 2):
                    matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]
            
        
        n = len(matrix)
        
        transpose(matrix)
        reflcet(matrix)
        
        
        
                
