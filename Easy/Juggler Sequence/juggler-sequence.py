#User function Template for python3

class Solution:
    def jugglerSequence(self, n):
        # code here
        k = [n]
        c = 0 
        while k[-1]!=1:
            if k[-1]%2==0:
                k.append(int(k[-1]**(1/2)))
            else:
                k.append(int(k[-1]**(3/2)))
            c =c + 1
        return k


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        arr = ob.jugglerSequence(n)
        for i in (arr):
            print(i, end=" ")
        print()

# } Driver Code Ends