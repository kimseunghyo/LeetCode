class Solution(object):
    def tree2str(self, root):
        def preorder(root):
            global result
            
            if root is None:
                return
            
            result += str(root.val)
            
            if root.left:
                result += "("
                preorder(root.left)
                result += ")"
                
            if root.right:
                if not root.left:
                    result += "()"
                
                result += "("
                preorder(root.right)
                result += ")"
           
        global result
        result = ""
            
        preorder(root)
        
        return result
        