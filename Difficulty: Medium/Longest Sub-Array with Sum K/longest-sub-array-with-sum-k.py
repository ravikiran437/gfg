#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, l, n, k) : 
        #Complete the function
        c = 0 
        d = {}
        m = 0 
        for i in range(len(l)):
            c += l[i]
            if c == k:
                m = max(i+1,m)
            if c not in d:
                d[c] = i 
            p = c - k
            if p in d:
                m = max(i-d[p],m)
        return m
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends