#User function Template for python3


#Function to modify the matrix such that if a matrix cell matrix[i][j]
#is 1 then all the cells in its ith row and jth column will become 1.
def booleanMatrix(mat):
    # code here 
    r,c=set(),set()
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]==1:
                r.add(i)
                c.add(j)
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]==0:
                if i in r:
                    mat[i][j]=1
                elif j in c:
                    mat[i][j]=1
            else:
                pass




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)
        booleanMatrix(matrix)
        for i in range(r):
            for j in range(c):
                print(matrix[i][j], end=' ')
            print()


# } Driver Code Ends