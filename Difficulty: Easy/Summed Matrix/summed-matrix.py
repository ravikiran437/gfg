#User function Template for python3

class Solution:
    def sumMatrix(self, n, q):
        # code here 
        a = n + 1 
        b = a + n - 1 
        if q > b:
            return 0
        if q <= a :
            return q-1
        if q > a:
            return b-q+1
        return 0
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())

        ob = Solution()
        print(ob.sumMatrix(n, q))

# } Driver Code Ends