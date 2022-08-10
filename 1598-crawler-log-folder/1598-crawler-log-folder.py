class Solution(object):
    def minOperations(self, logs):
        stack = []
        num = 0
        
        for lo in logs:
            if lo == "../":
                if stack:
                    stack.pop()
                    
            elif lo == "./":
                continue
            
            else:
                stack.append(lo)
                
        while stack:
            stack.pop()
            num += 1
            
        return num
                