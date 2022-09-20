class Solution(object):
    def findLength(self, nums1, nums2):
        len_n1 = len(nums1)
        len_n2 = len(nums2)
        
        dp = [[0] * (len_n2 + 1) for _ in range(len_n1 + 1)]

        for i in range(len_n1 - 1, -1, -1):
            for j in range(len_n2 - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                    
        return max(max(row) for row in dp)