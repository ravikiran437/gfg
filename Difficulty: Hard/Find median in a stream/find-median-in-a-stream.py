import bisect
class Solution:
    def getMedian(self, arr):
        sorted_list = []
        res = []
        for i, num in enumerate(arr):
            
            bisect.insort(sorted_list, num)
            
            n = i + 1  
            if n % 2 == 1:  
                median = float(sorted_list[n // 2])
            else:  
                median = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2.0
            
            res.append(median)
        
        return res
        