#User function Template for python3

class Solution:
    def ExcelColumn(self, n):
        #return required string
        #code here
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

if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        ob=Solution()
        print(ob.ExcelColumn(n))

# } Driver Code Ends