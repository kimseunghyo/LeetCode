class Solution(object):
    def levelOrderBottom(self, root):
        q = deque([root])
        res = deque([])
        
        while q:
            temp = []
            
            for i in range(len(q)):
                node = q.popleft()
                
                if node is None:
                    return 
                
                temp.append(node.val)
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                    
            res.appendleft(temp)
                    
        return res