#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,a,b):
        # code here
        a.sort()
        b.sort()
        i = 1
        p = 1
        j = 0
        while i < n:
            if a[i] > b[j]:
                j += 1 
            elif a[i] <= b[j]:
                p += 1 
            i = i + 1 
        return p
        
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
# } Driver Code Ends