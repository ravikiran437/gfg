#User function Template for python3

class Solution:
    # A1[] : the input array-1
    # 
    def relativeSort (self,A1, N, A2, M):
        # Your Code Here
        d = {}
        for i  in A1:
            if i not in d:
                d[i] = 1 
            else:
                d[i] += 1
        k = []
        for i in A2:
            if i in d:
                for j in range(d[i]):
                    k.append(i)
                del d[i]
        p = []
        for i,j in d.items():
            for m in range(j):
                p.append(i)
        p.sort()
        n = k + p
        for i in range(N):
            A1[i] = n[i]
        return A1
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int (input ())
    while t > 0:
        n, m = list(map(int, input().split()))
        a1 = list(map(int, input().split()))
        a2 = list(map(int, input().split()))
        
        ob=Solution()
        a1 = ob.relativeSort (a1, n, a2, m)
        print (*a1, end = " ")
        
        print ()
        
        t -= 1

# } Driver Code Ends