class Solution(object):
    def inorderTraversal(self, root):
        result = []
        
        def inorder(root):
            if root != None:
                if root.left:
                    inorder(root.left)

                result.append(root.val)

                if root.right:
                    inorder(root.right)

        inorder(root)
        
        
        return result
        