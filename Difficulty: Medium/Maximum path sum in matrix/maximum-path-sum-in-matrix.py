#User function Template for python3
#User function Template for python3

class Solution:
    def maximumPath(self, n,mat):
        # code here
        row = 0 
        col = n-1
        for i in range(1,n):
            for j in range(0,n):
                if j == 0:
                    m = max(mat[i-1][j],mat[i-1][j+1])
                    mat[i][j] += m 
                elif j == col:
                    m = max(mat[i-1][j],mat[i-1][j-1])
                    mat[i][j] += m 
                else:
                    m = max(mat[i-1][j],mat[i-1][j-1])
                    m = max(m,mat[i-1][j+1])
                    mat[i][j] += m 
        return max(mat[-1])

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        Matrix = [[0]*N for i in range(N)]
        for itr in range(N*N):
            Matrix[(itr//N)][itr%N] = int(arr[itr])
        
        ob = Solution()
        print(ob.maximumPath(N, Matrix))

# } Driver Code Ends