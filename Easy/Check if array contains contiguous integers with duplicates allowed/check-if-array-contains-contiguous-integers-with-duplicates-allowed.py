#User function Template for python3

class Solution:
    def areElementsContiguous (self, arr, n):
        d = {}
        for i in arr:
            if i not in d:
                d[i] = 1 
        l = list(d.keys())
        l.sort()
        for i in range(len(l)-1):
            if l[i+1]-l[i] != 1:
                return 0
        return 1
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    res = ob.areElementsContiguous(arr, n)
    if(res):
        print("Yes")
    else:
        print("No")



# } Driver Code Ends