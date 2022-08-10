class Solution(object):
    def decodeString(self, s):
        stack = []
        k = 0
        string = ''
        
        for char in s:
            if char.isdigit():
                k = k * 10 + int(char)
                            
            elif char == '[':
                stack.append(string)
                stack.append(k)
                
                string = ''
                k = 0
                
            elif char == ']':
                pre_k = stack.pop()
                pre_string = stack.pop()
                
                string = pre_string + pre_k * string
                
            else:
                string += char
                
        return string
                
        