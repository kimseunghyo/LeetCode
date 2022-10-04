class Solution(object):
    def hasPathSum(self, root, targetSum):
        global res
        res = False
        
        def dfs(root, sum_node):
            global res
            
            if root is None:
                return
            
            sum_node += root.val
            
            if sum_node == targetSum and root.left is None and root.right is None:
                res = True
            
            dfs(root.left, sum_node)
            dfs(root.right, sum_node)
            
            
        dfs(root, 0)
        
        return res
        
        
        