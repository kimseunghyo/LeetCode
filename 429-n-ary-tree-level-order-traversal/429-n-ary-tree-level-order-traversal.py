class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []
        
        result = []
        
        q = deque([root])
        
        while q:
            level = []
            
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                
                for child in node.children: 
                    q.append(child)
                
            result.append(level)
            
        return result
                
        
        