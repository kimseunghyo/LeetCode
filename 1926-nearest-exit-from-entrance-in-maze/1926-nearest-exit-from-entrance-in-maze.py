class Solution(object):
    def nearestExit(self, maze, entrance):
        def bfs(r, c):
            q = deque([(r, c)])
            maze[r][c] = 0
            
            while q:
                r, c = q.popleft()
                
                if maze[r][c] != 0 and (r == m - 1 or r == 0 or c == n - 1 or c == 0):
                    return maze[r][c]
                
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    
                    if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == '.':
                        maze[nr][nc] = maze[r][c] + 1
                        q.append((nr, nc))
                        
            return -1           
                    
        m = len(maze)
        n = len(maze[0])
            
        dr = [1, 0, -1, 0]
        dc = [0, 1, 0, -1]
        
        return bfs(entrance[0], entrance[1])
        