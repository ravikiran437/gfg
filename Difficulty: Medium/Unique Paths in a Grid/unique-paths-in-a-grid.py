#User function Template for python3

class Solution:
    def uniquePaths(self, n, m, grid):
        # code here 
        mod = (10**9)+7
        for i in range(1,m):
            grid[0][i] = min(grid[0][i],grid[0][i-1])
        for j in range(1,n):
            grid[j][0] = min(grid[j][0],grid[j-1][0])
        for i in range(1,n):
            for j in range(1,m):
                if grid[i][j] == 1:
                    grid[i][j] = (grid[i][j-1]+grid[i-1][j])%mod
        # print(grid)
        return grid[-1][-1] % mod


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n,m=map(int,input().split())
        
        grid=[]
        for i in range(n):
            col = list(map(int,input().split()))
            grid.append(col)
        
        ob = Solution()
        print(ob.uniquePaths(n,m,grid))
# } Driver Code Ends