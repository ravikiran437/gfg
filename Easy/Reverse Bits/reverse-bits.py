#User function Template for python3

class Solution:
    def reversedBits(self, X):
        a=(bin(X)[2:])
        b=32-len(a)
        k=""
        for i in range(b):
            k+='0'
        k=k+a
        s=k[::-1]
        return int(s,2)
        





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        X=int(input())
        
        ob = Solution()
        print(ob.reversedBits(X))
# } Driver Code Ends