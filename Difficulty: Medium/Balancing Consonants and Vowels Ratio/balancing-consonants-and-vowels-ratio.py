from collections import defaultdict
class Solution:
    def countBalanced(self, arr):
        # code here
        def calc(s):
            v,c = 0,0
            for i in s:
                if i in "aeiou":
                    v += 1 
                else:
                    c += 1 
            return v,c 
        
        d = defaultdict(int)
        d[0] = 1
        count = 0 
        total_v,total_c = 0,0
        for word in arr:
            v,c = calc(word)
            total_v += v
            total_c += c
            diff = total_v - total_c
            count += d[diff]
            d[diff] += 1

        return count