class Solution(object):
    def scoreOfParentheses(self, s):
        stack = []
        cur = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(cur)
                cur = 0
                
            else:
                cur = stack.pop() + max(cur * 2, 1)
                
        return cur
                
        