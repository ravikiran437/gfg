# Your task is to complete this function

class Solution:
    def matrixDiagonally(self,l):
        # code here
        k = []
        for i in range(len(l)+len(l)-1):
            k.append([])
        for i in range(len(l)):
            for  j in range(len(l)):
                k[i+j].append(l[i][j])
        l1 = []
        for i in range(len(k)):
            if i%2==0:
                k[i] = k[i][::-1] 
            l1 += k[i] 
        return l1


#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        a = Solution().matrixDiagonally(matrix)
        for x in a:
            print(x,end=' ')
        print('')
# Contributed by: Harshit Sidhwa
# } Driver Code Ends