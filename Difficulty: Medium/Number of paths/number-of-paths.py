class Solution:
    def numberOfPaths(self, m, n):
        # code here
        mat = []
        for i in range(m):
            mat.append([1]*n)
        for i in range(1,m):
            for j in range(1,n):
                mat[i][j] = mat[i-1][j] + mat[i][j-1]
        return mat[-1][-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        M, N = map(int, input().split())
        ans = ob.numberOfPaths(M, N)
        print(ans)

        print("~")

# } Driver Code Ends