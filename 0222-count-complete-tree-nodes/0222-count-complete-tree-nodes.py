class Solution(object):
    def countNodes(self, root):
        q = deque([root])
        res = 1
        
        if root is None:
            return 0
        
        for i in range(len(q)):
            while q:
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                    res += 1
                    
                if node.right:
                    q.append(node.right)
                    res += 1
                    
        return res