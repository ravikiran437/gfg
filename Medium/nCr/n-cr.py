#User function Template for python3
import math
class Solution:
    def nCr(self, n, r):
        def fact(n):
            if n==0:
                return 1
            return n*fact(n-1)
        if r>n:
            return 0
        m=(10**9)+7
        return (fact(n)//(fact(r)*fact(n-r)))%m
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nCr(n, r))
# } Driver Code Ends