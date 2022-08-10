class Solution(object):
    def isValidBST(self, root):
        stack = []
        
        def Inorder(root):
            if root != None:
                if root.left:
                    Inorder(root.left)

                stack.append(root.val)

                if root.right:
                    Inorder(root.right)


        Inorder(root)
        
        while stack and len(stack) > 1:
            temp = stack.pop()
            
            if stack[-1] >= temp:
                return False
        
        return True
        