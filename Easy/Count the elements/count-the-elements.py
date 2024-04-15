#User function Template for python3
import bisect
class Solution:
    def countElements(self, a, b, n, query, q):
        # code here
        b.sort()
        k = []
        for i in query:
            p = a[i]
            k.append(bisect.bisect_right(b, p))
        return k
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    q = int(input())
    query = []
    ob = Solution()
    for i in range(q):
        query.append(int(input()))
    ans = ob.countElements(a, b, n, query, q)
    for i in range(q):
        print(ans[i])

# } Driver Code Ends