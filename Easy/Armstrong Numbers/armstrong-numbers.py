#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        temp = n
        c = 0 
        while n :
            p = n%10
            c += (p**3)
            n = n//10 
        if c == temp:
            return "Yes"
        return "No"


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends