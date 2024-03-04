#User function Template for python3
class Solution:

    def checkTriplet(self,l, n):
        # code here
        s = set(l)
        k=[]
        for i in s:
            k.append(i**2)
        l =list(s)
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                c=l[i]**2 +l[j]**2
                if c in k:
                    return 1 
        return 0





#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.checkTriplet(arr, n)
        if ans:
            print("Yes")
        else:
            print("No")
        tc -= 1

# } Driver Code Ends