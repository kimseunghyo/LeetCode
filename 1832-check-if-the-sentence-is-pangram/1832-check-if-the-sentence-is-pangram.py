class Solution(object):
    def checkIfPangram(self, sentence):
        if len(set(sentence)) == 26:
            return True
        
        return False
        
        