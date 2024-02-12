#User function Template for python3

class Solution:
    def sequence(self, n):
        # code here
        c = 0 
        m = 1
        s =set()
        l = 0
        mod = (10**9)+7
        for i in range(1,((n*(n+1))//2)+1):
            m = m * i 
            c = c+1
            if c not in s:
                s.add(c)
                l += (m) % mod
                m = 1
                c = 0 
        return l % mod



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.sequence(N))
# } Driver Code Ends