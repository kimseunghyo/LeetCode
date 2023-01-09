class Solution(object):
    def preorderTraversal(self, root):
        res = []
        
        def dfs(root):
            if root is None:
                return
            
            res.append(root.val)
            
            if root.left:
                dfs(root.left)
            
            if root.right:
                dfs(root.right)
                
        
        dfs(root)
        
        return res
        