class Solution:
    def celebrity(self, mat):
        for i in range(len(mat[0])):
            c = 0 
            for j in range(len(mat)):
                if mat[j][i] == 1:
                    c += 1 
                else:
                    r = i
            if c == len(mat)-1 :
                if mat[r].count(1) == 0 :
                    return r 
        return -1
                

#{ 
 # Driver Code Starts
# Main function to handle input and output
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        M = []
        for _ in range(n):
            M.append(list(map(int, input().split())))

        ob = Solution()
        print(ob.celebrity(M))

# } Driver Code Ends