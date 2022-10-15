class Solution(object):
    def removeDuplicates(self, s, k):
        res = ""
        stack = []
        stack.append([s[0], 1])
        
        for i in range(1, len(s)):
            if stack and s[i] == stack[-1][0]:
                if stack[-1][1] == k - 1:
                    while stack and stack[-1][0] == s[i]:
                        stack.pop()

                else:
                    stack.append([s[i], stack[-1][1] + 1])

            else:
                stack.append([s[i], 1])
                
        for c in stack:
            res += c[0]
            
        return res                     