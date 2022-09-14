class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        dic = {}
        cnt = 0
        
        for n1 in nums1:
            for n2 in nums2:
                if (n1 + n2) in dic:
                    dic[n1 + n2] += 1
                    
                else:
                    dic[n1 + n2] = 1
                    
        for n3 in nums3:
            for n4 in nums4:
                if (-n3 - n4) in dic:
                    cnt += dic[-n3 - n4]
                    
        return cnt
        
        