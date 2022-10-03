class Solution(object):
    def minCost(self, colors, neededTime):
        res = 0
        stack = []
        stack.append(0)

        for i in range(1, len(colors)):
            if colors[i] == colors[stack[-1]]:
                if neededTime[i] < neededTime[stack[-1]]:
                    res += neededTime[i]
                    
                else:
                    res += neededTime[stack.pop()]
                    stack.append(i)
            
            else:
                stack.append(i)
                
        return res
            
        