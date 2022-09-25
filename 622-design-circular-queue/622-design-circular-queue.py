class MyCircularQueue(object):

    def __init__(self, k):
        self.q = [None] * k
        self.p1 = 0
        self.p2 = 0
        self.size = k
        

    def enQueue(self, value):
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.size
            
            return True
            
        else:
            return False
            
        

    def deQueue(self):
        if self.q[self.p1] is not None:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.size
            
            return True
        
        else:
            return False
        
        

    def Front(self):
        return self.q[self.p1] if self.q[self.p1] is not None else -1
        

    def Rear(self):
        return self.q[self.p2 - 1] if self.q[self.p2 - 1] is not None else -1
        

    def isEmpty(self):
        return True if self.p1 == self.p2 and self.q[self.p1] is None else False
        

    def isFull(self):
        return True if self.p1 == self.p2 and self.q[self.p1] is not None else False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()