class Solution(object):
    def frequencySort(self, s):
        count = Counter(s)
        sort_c = sorted(count.items(), key=lambda x:(-x[1], x[0]))
        
        return "".join(sort_c[i][0] * sort_c[i][1] for i in range(len(sort_c)))
        