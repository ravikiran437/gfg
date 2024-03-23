#User function Template for python3

class Solution:
    def series(self, n):
        # Code her
        a,b = 0,1
        l = [a,b]
        m = (10**9)+7
        for i in range(n-1):
            c = (a%m+b%m)%m
            l.append(c)
            a = b%m
            b = c%m
        return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        result = ob.series(N)
        print(*result)
# } Driver Code Ends