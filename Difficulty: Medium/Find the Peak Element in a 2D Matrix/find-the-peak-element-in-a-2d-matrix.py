class Solution:
    def findPeakGrid(self, mat):
        # code here
        for row in range(len(mat)):
            for col in  range(len(mat[0])):
                maxi = float("-inf")
                for i,j in [(0,-1),(0,1),(-1,0),(1,0)]:
                    r = row + i 
                    c =  col + j 
                    if r >= 0 and c >= 0 and r < len(mat) and  c < len(mat[0]):
                        maxi = max(maxi,mat[r][c])
                if mat[row][col] >= maxi:
                    return [row,col]
        return [-1,-1]