#User function Template for python3

from collections import OrderedDict
class Solution:
    def findMissing(self,A,B,n,m):
        l1 = []
        B = set(B)
        for i in A:
            if i not in B:
                l1.append(i)
        return l1
                
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
   # n=int(input())
    l = list(map(int, input().split()))
    n=l[0]
    m=l[1]
    a = list(map(int,input().split()))
    b = list(map(int, input().split()))
    ob=Solution()
    ans=ob.findMissing(a,b,n,m)
    for each in ans:
        print(each,end=' ')
    print()
# } Driver Code Ends