#User function Template for python3

class Solution:
	def FindExitPoint(self, n, m, mat):
		# Code here
		i = 0 
        j = 0
        k = []
        if mat[0][0] == 0 :
            pos = "st"
            j += 1
        else:
            pos = "dn"
            i += 1
        while i<len(mat) and j<len(mat[0]) and i!=-1 and j!=-1:
            k.append([i,j])
            if mat[i][j] == 1 and pos == "st" :   
                mat[i][j] = 0 
                i += 1
                pos = "dn"
            elif mat[i][j] == 1 and pos == "dn":
                mat[i][j] = 0 
                j = j -1
                pos = "lf"
            elif mat[i][j] == 0 and pos == "lf":
                j = j-1
                pos = "lf"
            elif mat[i][j] == 1 and pos == "lf":
                mat[i][j] = 0 
                i -= 1 
                pos ="up"
            elif mat[i][j] == 0 and pos =="up":
                i -= 1
                pos = "up"
            elif mat[i][j] == 0 and pos =="st":
                j += 1 
                pos = "st"
            elif mat[i][j] == 0 and pos == "dn":
                i += 1 
                pos = "dn"
            elif mat[i][j] == 1 and pos == "up":
                mat[i][j] = 0
                j += 1 
                pos = "st"
        if k :
            return k[-1]
        return [0,0]
    		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        ob = Solution()
        ans = ob.FindExitPoint(n, m, matrix)
        for _ in ans:
            print(_, end=" ")
        print()

# } Driver Code Ends