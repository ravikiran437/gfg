from typing import List


class Solution:
    def finLength(self, N : int, c : List[int], r : List[int]) -> int:
        # code here
        k=[]
        for i,j in zip(c,r):
            if k == []:
                k.append((i,j))
            elif k[-1] == (i,j):
                k.pop()
            else:
                k.append((i,j))
        return len(k)



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
        
        N = int(input())
        
        
        color=IntArray().Input(N)
        
        
        radius=IntArray().Input(N)
        
        obj = Solution()
        res = obj.finLength(N, color, radius)
        
        print(res)
        

# } Driver Code Ends