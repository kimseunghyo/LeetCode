class Solution(object):
    def permuteUnique(self, nums):
        return set(permutations(nums))