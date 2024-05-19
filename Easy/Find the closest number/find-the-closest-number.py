
from typing import List


class Solution:
    def findClosest(self, n : int, k : int, arr : List[int]) -> int:
        # code here
        d = {}
        for i in arr:
            kk = abs(i-k)
            if i not in d:
                d[i] = kk
        m = min(d.values())
        # print(d)
        maxi = float("-inf")
        for i,j in d.items():
            if j == m:
                maxi = max(maxi,i)
        return maxi
                
        



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        k = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.findClosest(n, k, arr)
        
        print(res)
        

# } Driver Code Ends