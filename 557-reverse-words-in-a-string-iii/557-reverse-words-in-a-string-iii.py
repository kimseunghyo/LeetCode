class Solution(object):
    def reverseWords(self, s):
        stack = []
        res = []
        
        for c in s:
            if c == " ":
                while stack:
                    res.append(stack.pop())
                    
                res.append(" ")
                
            else:
                stack.append(c)
                
        return "".join(res + stack[::-1])
        