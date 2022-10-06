class TimeMap(object):

    def __init__(self):
        self.dic = {}

    def set(self, key, value, timestamp):
        if key not in self.dic:
            self.dic[key] = []
            
        self.dic[key].append([timestamp, value])

    def get(self, key, timestamp):
        if key not in self.dic:
            return ""
        
        left = 0
        right = len(self.dic[key])
        
        while left < right:
            mid = (left + right) // 2
            
            if self.dic[key][mid][0] <= timestamp:
                left = mid + 1
                
            else:
                right = mid
        
        
        return self.dic[key][right - 1][1] if right != 0 else ""
