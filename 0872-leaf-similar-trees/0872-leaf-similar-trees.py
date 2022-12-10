class Solution(object):
    def leafSimilar(self, root1, root2):
        def dfs(root, leaf):
            if root is None:
                return
            
            if not root.left and not root.right:
                leaf.append(root.val)
            
            dfs(root.left, leaf)
            dfs(root.right, leaf)
            
            return leaf
        
        
        return True if dfs(root1, []) == dfs(root2, []) else False
        