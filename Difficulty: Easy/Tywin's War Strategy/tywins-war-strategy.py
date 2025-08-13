import math
class Solution:
    def minSoldiers(self, arr, k):
        # code here
        n = math.ceil(len(arr) / 2)
        
        count = 0
        l = []
        for num in arr:
            if num % k == 0:
                count += 1 
            else:
                l.append(k - (num % k))
        req = n - count 
       
        if req <= 0:
            return 0 
        l.sort()
    
        return sum(l[:req])
        