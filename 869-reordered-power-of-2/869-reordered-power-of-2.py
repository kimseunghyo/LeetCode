class Solution(object):
    def reorderedPowerOf2(self, n):
        re_n = permutations(str(n))
        
        for re in re_n:
            if re[0] != '0' and bin(int("".join(re))).count('1') == 1:
                return True
            
        return False