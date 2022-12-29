class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return 
        
        q = deque([root])
        res = []
        
        while q:
            path = []
            
            for i in range(len(q)):
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                    
                path.append(node.val)
                    
                if node.right:
                    q.append(node.right)
                    
            res.append(path)
                
        return res
        