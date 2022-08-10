class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        
        queue = collections.deque([root])
        depth = 0
        
        while queue:
            depth += 1
            
            for _ in range(len(queue)):
                cur_queue = queue.popleft()
                
                if cur_queue.left:
                    queue.append(cur_queue.left)
                if cur_queue.right:
                    queue.append(cur_queue.right)
                
                
        return depth
        