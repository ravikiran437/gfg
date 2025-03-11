
class Solution:
    def countWays(self, n):
        # code here
        if n == 1:
            return 1
        a = 1
        b = 1
        for i in range(n-1):
            c = a+b
            a = b
            b = c
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob = Solution()
        print(ob.countWays(m))

        print("~")

# } Driver Code Ends