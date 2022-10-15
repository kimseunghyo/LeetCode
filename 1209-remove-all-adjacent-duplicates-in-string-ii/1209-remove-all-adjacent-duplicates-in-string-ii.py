class Solution(object):
    def removeDuplicates(self, s, k):
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
                
        return "".join(c[0] for c in stack)      