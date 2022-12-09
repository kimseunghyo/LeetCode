class Solution(object):
    def maxAncestorDiff(self, root):
        def dfs(root, max_n, min_n):
            if root is None:
                return
            
            if root.val > max_n:
                max_n = root.val
                
            if root.val < min_n:
                min_n = root.val
                
            if max_n - min_n > self.res:
                self.res = max_n - min_n
            
            dfs(root.left, max_n, min_n)
            dfs(root.right, max_n, min_n)
            
        
        self.res = 0
        
        dfs(root, root.val, root.val)
        
        return self.res