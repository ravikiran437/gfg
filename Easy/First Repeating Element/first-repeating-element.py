#User function Template for python3

class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,l, n):
        
        k = {}
        c = 1
        m = float("+inf")
        for i in l:
            if i not in k:
                k[i] = c
            else:
                m = min(m,k[i])
            c += 1 
        if m == float("+inf"):
            return -1 
        return m

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstRepeated(arr, n))
# } Driver Code Ends