class Solution:
    def searchMatrix(self, mat, x):
        # code here
        for row in mat:
            if x in row:
                return True
        return False