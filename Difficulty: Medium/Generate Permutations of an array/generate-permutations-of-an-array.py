from itertools import permutations
class Solution:
    def permuteDist(self, arr):
        # code here
        return list(set(permutations(arr)))
        
        
        