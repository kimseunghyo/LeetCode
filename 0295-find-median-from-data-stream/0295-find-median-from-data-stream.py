class MedianFinder(object):

    def __init__(self):
        self.max_hq = []
        self.min_hq = []

        
    def addNum(self, num):
        if len(self.max_hq) == len(self.min_hq):
            heappush(self.max_hq, -heappushpop(self.min_hq, -num))
            
        else:
            heappush(self.min_hq, -heappushpop(self.max_hq, num))
        

    def findMedian(self):
        if len(self.max_hq) == len(self.min_hq):
            return float(self.max_hq[0] - self.min_hq[0]) / 2
        
        else:
            return float(self.max_hq[0])
        