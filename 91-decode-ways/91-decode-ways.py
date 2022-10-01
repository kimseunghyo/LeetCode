class Solution(object):
    def numDecodings(self, s):
        if s[0] == '0':
            return 0
        
        len_s = len(s)
    
        dp = [0] * (len_s + 1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, len_s + 1):
            if s[i - 2] == '1' or (s[i - 2] == '2' and int(s[i - 1]) <= 6):
                dp[i] += dp[i - 2]
                
            if s[i - 1] == '0':
                if s[i - 2] != '1' and s[i - 2] != '2':
                    return 0
                
            else:
                dp[i] += dp[i - 1]
                    
        return dp[len_s]
                
            