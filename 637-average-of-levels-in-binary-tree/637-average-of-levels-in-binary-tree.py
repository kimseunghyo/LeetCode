class Solution(object):
    def averageOfLevels(self, root):
        result = []
        
        if root is None:
            return 
        
        q = deque([root])
        
        while q:
            len_q = len(q)
            sum_n = 0
            
            for _ in range(len_q):
                node = q.popleft()
                sum_n += float(node.val)
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                    
            result.append(sum_n / len_q)
                
                
        return result