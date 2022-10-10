class Solution(object):
    def findTarget(self, root, k):
        nodes = []
        
        def inorder(root):
            if root is None:
                return
            
            if root.left:
                inorder(root.left)
                
            nodes.append(root.val)
                
            if root.right:
                inorder(root.right)
            
        
        inorder(root)
        
        left = 0
        right = len(nodes) - 1
        
        while left < right:
            sum_n = nodes[left] + nodes[right]
            
            if sum_n == k:
                return True
            
            if sum_n < k:
                left +=1
            
            else:
                right -= 1
        
        return False