#User function Template for python3

class Solution:
    def recamanSequence(self, n):
        # code here
        l  = [0]*n
        s = set()
        for i in range(1,n):
            k = l[i-1] - i
            if k>0 and k not in s:
                s.add(k)
                l[i] = k
            else:
                l[i] = l[i-1] + i 
                s.add(l[i-1]+i)
        return l
        
        





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.recamanSequence(n)
        for i in range(n):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends