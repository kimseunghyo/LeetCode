class Solution(object):
    def generateParenthesis(self, n):        
        result = []
        
        def backtracking(s, left, right):
            if len(s) == 2 * n:
                result.append("".join(s))
                
                return
            
            if left < n:
                s.append("(")
                backtracking(s, left + 1, right)
                s.pop()
                
            if right < left:
                s.append(")")
                backtracking(s, left, right + 1)
                s.pop()
                
        backtracking([], 0, 0)
        
        return result
        