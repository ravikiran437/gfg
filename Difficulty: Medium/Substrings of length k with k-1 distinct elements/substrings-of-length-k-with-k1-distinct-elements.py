#User function Template for python3
from collections import deque
class Solution:
    def countOfSubstrings(self, s, k):
        # code here 
        d = {}
        l = deque()
        c = 0 
        for i in range(len(s)):
            if l and l[0] <  i-k+1:
                d[s[l[0]]] -= 1 
                if d[s[l[0]]] == 0:
                    del d[s[l[0]]]
                l.popleft()
            l.append(i)
            if s[i] not in d:
                d[s[i]] = 1 
            else:
                d[s[i]] += 1 
            if i >= k-1:
                if len(d) == k-1:
                    c += 1 
        return c
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        K=int(input())
        
        ob = Solution()
        print(ob.countOfSubstrings(S,K))
# } Driver Code Ends