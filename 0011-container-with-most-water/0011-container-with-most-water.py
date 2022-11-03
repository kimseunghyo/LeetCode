class Solution(object):
    def maxArea(self, height):
        p1 = 0
        p2 = len(height) - 1
        
        max_a = 0
        
        while p1 < p2:
            if height[p1] < height[p2]:
                area = height[p1] * (p2 - p1)
                p1 += 1
            
            else:
                area = height[p2] * (p2 - p1)
                p2 -= 1
            
            if area > max_a:
                max_a = area
                
        return max_a
        