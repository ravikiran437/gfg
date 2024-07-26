#User function Template for python3

class Solution:
    def colName (self, n):
        s = ""
        while n:
            k = n%26
            if k == 0:
                s += "Z"
            else:
                s += chr(k+64)
            if k == 0:
                n = (n//26)-1
            else:
                n = n//26
        return s[::-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n = int (input ())
    ob = Solution()
    print (ob.colName (n))
    

# } Driver Code Ends