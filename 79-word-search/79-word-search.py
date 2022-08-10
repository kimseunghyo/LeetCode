class Solution(object):
    def exist(self, board, word):
        def dfs(r, c, word):
            if not word:
                return True
            
            temp = board[r][c]
            board[r][c] = '#'
            
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != '#':
                    if board[nr][nc] == word[0]:
                        if dfs(nr, nc, word[1:]):
                            return True
                        
            board[r][c] = temp
                
            return False
        
        
        m, n = len(board), len(board[0])
        
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, word[1:]):
                        return True
        