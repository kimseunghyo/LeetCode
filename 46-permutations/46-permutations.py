class Solution(object):
    def permute(self, nums):
        result = []

        def dfs(n, path):
            if len(n) == 0:
                result.append(path + n)

            for i in range(len(n)):
                dfs(n[:i] + n[i + 1:], path + [n[i]])
            
        dfs(nums, [])
            
        return result
        