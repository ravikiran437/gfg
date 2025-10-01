from itertools import permutations
class Solution:
    def uniquePerms(self, arr):
        # code here 
        k=list(permutations(arr))
        d={}
        for i in k:
            if i not in d:
                d[i]=1 
        s=[]
        for i in d.keys():
            s.append(i)
        s.sort()
        return s