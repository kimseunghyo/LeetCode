class Solution(object):
    def rangeSumBST(self, root, low, high):     
        def dfs(root): 
            if root is None:
                return
            
            if low <= root.val <= high:
                self.sum_n += root.val
            
            if root.val > low:
                dfs(root.left)
                
            if root.val < high:
                dfs(root.right)
                
                
        self.sum_n = 0
        
        dfs(root)
        
        return self.sum_n
        