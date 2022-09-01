class Solution(object):
    def goodNodes(self, root):
        good = []
        
        global cnt
        cnt = 0
        
        def dfs(root, rv):
            global cnt
            
            if root == None:
                return 
            
            if rv <= root.val:
                cnt += 1
                rv = root.val
                
            dfs(root.left, rv)
            dfs(root.right, rv)
            
                  
        dfs(root, root.val)
        
        return cnt
        
                    
                    
        