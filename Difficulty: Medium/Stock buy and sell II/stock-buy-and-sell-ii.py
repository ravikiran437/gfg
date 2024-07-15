
from typing import List


class Solution:
    def stockBuyAndSell(self, n : int, nums : List[int]) -> int:
        # code here
        a = nums[0]
        cnt = 0 
        maxi = 0 
        for i in nums[1:]:
            if maxi == 0 and a > i :
                a = i 
            else:
                if maxi > i :
                    cnt += maxi - a 
                    a = i 
                    maxi = 0 
                else:
                    maxi = i 
        if maxi !=0 :
            cnt += maxi-a
        return cnt
        
        



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
        
        
        prices=IntArray().Input(n)
        
        obj = Solution()
        res = obj.stockBuyAndSell(n, prices)
        
        print(res)
        

# } Driver Code Ends