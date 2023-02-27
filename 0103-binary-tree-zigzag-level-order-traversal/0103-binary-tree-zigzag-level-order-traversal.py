class Solution(object):
    def zigzagLevelOrder(self, root):
        res = []
        q = deque([root])
        depth = 0
        
        if root is None:
            return 
        
        while q:
            level = []
            depth += 1
            
            for i in range(len(q)):
                if depth % 2 == 0:
                    node = q.popleft() 
                    
                    if node.right:
                        q.append(node.right)
                    if node.left:
                        q.append(node.left)
                    
                else:
                    node = q.pop()
        
                    if node.left:
                        q.appendleft(node.left)
                    if node.right:
                        q.appendleft(node.right)
                
                level.append(node.val)
                
            res.append(level)
                
        return res
        