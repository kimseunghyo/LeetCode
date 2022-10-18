class Solution(object):
    def countAndSay(self, n):
        string = "1"
        
        for i in range(2, n + 1): 
            temp = ""
            prev_c = string[0]
            cnt = 0
            
            for cur_c in string:
                if cur_c == prev_c:
                    cnt += 1
                    
                else:
                    temp += str(cnt) + prev_c
                    prev_c = cur_c
                    cnt = 1
            
            temp += str(cnt) + prev_c
            string = temp
            
        return string