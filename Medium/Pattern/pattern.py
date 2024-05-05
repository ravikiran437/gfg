#User function Template for python3

class Solution:
    def printDiamond(self, N):
        # Code here
        for i in range(1,N+1):
            if i == N:
                print("* "*i)
            else:
                c = N-i-1
                s  = ((" "*c)+ (" *"*i))
                print(s)
        for i in range(N,0,-1):
            if i == N:
                print("* "*i)
            else:
                c = N-i-1
                s  = ((" "*c)+ (" *"*i))
                print(s)
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printDiamond(N)
# } Driver Code Ends