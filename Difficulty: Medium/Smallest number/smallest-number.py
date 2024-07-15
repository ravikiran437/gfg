#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def smallestNumber (self, n, k):
        # code here
        if (9*k) < n:
            return -1
        c = 0 
        s = [9]*k
        for i in range(len(s)-1):
            if n>s[i]:
                n = n - s[i]
            elif n<=s[i] and c == 0:
                s[i] = n - 1 
                n = n - s[i]
                c = 1 
            else:
                s[i] = 0 
        s[-1] = n
        s = s[::-1]
        p = 0
        for i in s:
            p = p*10 + i 
        return p





#{ 
 # Driver Code Starts.
# Position this line where user code will be pasted.

import sys
import math
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1

for _ in range(t):
    s = int(data[index])
    d = int(data[index + 1])
    index += 2
    ob = Solution()
    print(ob.smallestNumber(s, d))

# } Driver Code Ends