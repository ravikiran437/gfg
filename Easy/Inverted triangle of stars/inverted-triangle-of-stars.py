#User function Template for python3

class Solution:
    def invIsoTriangle(self, N):
        # code here 
        s = []
        b = 2
        k = ""
        for i in range(N,0,-1):
            a = (i*2)-1
            if i == N:
                k = "*"*a
            else:
                k = " "*b+"*"*a+" "*b
                b += 1
            s.append(k)
        return s
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        ans=(ob.invIsoTriangle(N))
        for i in ans:
            print(i)
# } Driver Code Ends