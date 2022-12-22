class Solution(object):
    def numTilePossibilities(self, tiles):
        res = set()
        
        def dfs(path, t):
            if path not in res:
                if len(path) > 0:
                    res.add(path)
                    
                for i in range(len(t)):
                    dfs(path + t[i], t[:i] + t[i + 1:])
                
        
        dfs("", tiles)
        
        return len(res)