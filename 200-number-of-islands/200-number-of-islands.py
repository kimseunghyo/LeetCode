class Solution(object):
    from collections import deque
    
    def numIslands(self, grid):
        def bfs(r, c):
            q = deque([(r, c)])
            
            while q:
                r, c = q.popleft()
                
                grid[r][c] = '2'

                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]

                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                        bfs(nr, nc)
                    
            
        m = len(grid)
        n = len(grid[0])
        
        dr = [1, 0, -1, 0]
        dc = [0, 1, 0, -1]
        
        num = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    bfs(i, j)
                    
                    num += 1
                    
        return num