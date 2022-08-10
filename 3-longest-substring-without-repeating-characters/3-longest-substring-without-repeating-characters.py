class Solution(object):
    def lengthOfLongestSubstring(self, s):
        used = {}
        max_len = 0
        start = 0
        
        for index, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
                
            else:
                max_len = max(max_len, index - start + 1)
                
            used[char] = index
            
        return max_len