class Solution:
    def isProduct(self, arr, target):
        # code here
        arr.sort()
        i,j = 0,len(arr)-1
        
        while i < j :
            ans = arr[i] * arr[j] 
            if ans == target :
                return True
            elif ans > target:
                j -= 1 
            else:
                i += 1 
        return False