class Solution(object):
    def pathSum(self, root, targetSum):
        res = []
        
        def dfs(root, sum_node, path):
            if root is None:
                return
            
            sum_node += root.val
            
            if sum_node == targetSum and root.left is None and root.right is None:
                res.append(path + [root.val])
            
            dfs(root.left, sum_node, path + [root.val])
            dfs(root.right, sum_node, path + [root.val])
            
        
        dfs(root, 0, [])
        
        return res