#User function Template for python3

class Solution:
    def minValue(self, s, k):
        # code here\
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1 
        l = list(d.values())
        l.sort()
        c = 0 
        while k > 0 :
            l[-1] = l[-1] - 1 
            k = k - 1 
            l.sort()
        for i in l:
            c += (i**2)
        return c

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        k = int(input())
        
        ob = Solution()
        print(ob.minValue(s, k))
# } Driver Code Ends