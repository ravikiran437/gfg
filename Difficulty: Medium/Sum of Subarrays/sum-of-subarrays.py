class Solution:
    def subarraySum(self, arr):
        # code here 
        total = 0 
        for i in range(len(arr)):
            start = i + 1 
            end = len(arr) - i  
            total += (arr[i] * (start*end))
        return total
        