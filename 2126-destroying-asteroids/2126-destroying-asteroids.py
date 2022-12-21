class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        for a in sorted(asteroids):
            if mass >= a:
                mass += a
                
            else:
                return False
            
        return True