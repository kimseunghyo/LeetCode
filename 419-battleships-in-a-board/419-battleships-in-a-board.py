class Solution(object):
    def countBattleships(self, board):
        def dfs(r, c):
            board[r][c] = '.'
                
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                    
                if 0 <= nr < m and 0 <= nc < n:
                    if board[nr][nc] == 'X':
                        dfs(nr, nc)
            
            
        m = len(board)
        n = len(board[0])
        
        num = 0
        
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    dfs(i, j)
                    num += 1
                    
        return num
        