class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        width1 = (ax2 - ax1)
        height1 = (ay2 - ay1)
        
        width2 = (bx2 - bx1)
        height2 = (by2 - by1)
        
        width3 = max(min(ax2, bx2) - max(ax1, bx1), 0)
        height3 = max(min(ay2, by2) - max(ay1, by1), 0)
        
        rec1 = width1 * height1
        rec2 = width2 * height2
        rec3 = width3 * height3
        
        return rec1 + rec2 - rec3
    
        