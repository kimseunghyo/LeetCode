class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        operands = ['+', '-', '*', '/']
        
        for tkn in tokens:
            if tkn in operands:
                n2 = stack.pop()
                n1 = stack.pop()
            
                if tkn == '+':
                    stack.append(n1 + n2)

                if tkn == '-':
                    stack.append(n1 - n2)

                if tkn == '*':
                    stack.append(n1 * n2)

                if tkn == '/':  
                    stack.append(int(float(n1) / n2))
            
            else:
                stack.append(int(tkn))
                
        return stack[0]
        