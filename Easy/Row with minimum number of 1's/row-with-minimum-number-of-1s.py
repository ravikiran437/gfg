#User function Template for python3

class Solution:
    def minRow(self,n,m,a):
        #code here
        m = float("inf")
        c =  0 
        for i in a:
            m = min(m,i.count(1))
        for i in range(n):
            if a[i].count(1) == m:
                return i+1
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(" "))
        A=[]
        for i in range(N):
            B=list(map(int,input().strip().split(" ")))
            A.append(B)
        ob=Solution()
        print(ob.minRow(N,M,A))
# } Driver Code Ends