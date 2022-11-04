class Solution(object):
    def reverseVowels(self, s):
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        c = list(s)

        p1 = 0
        p2 = len(s) - 1

        while p1 < p2:
            if c[p1] in vowels and c[p2] in vowels:
                c[p1], c[p2] = c[p2], c[p1]
                p1 += 1
                p2 -= 1

            if c[p1] not in vowels:
                p1 += 1
            
            if c[p2] not in vowels:
                p2 -= 1

        return "".join(c)