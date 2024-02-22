#User function Template for python3
class Solution:
    def smallestNumber (self, n, k):
        # code here
        if (9*k) < n:
            return -1
        c = 0 
        s = [9]*k
        for i in range(len(s)-1):
            if n>s[i]:
                n = n - s[i]
            elif n<=s[i] and c == 0:
                s[i] = n - 1 
                n = n - s[i]
                c = 1 
            else:
                s[i] = 0 
        s[-1] = n
        s = s[::-1]
        p = ""
        for i in s:
            p += str(i)
        return int(p)



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S,D=map(int,input().strip().split(" "))

        ob = Solution()
        print(ob.smallestNumber(S,D))
# } Driver Code Ends