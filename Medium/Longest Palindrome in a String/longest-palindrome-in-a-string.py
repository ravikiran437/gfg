#User function Template for python3

class Solution:
    def longestPalin(self, s):
        # code here
        k = len(s)
        for i in range(k):
            c = k-i-1
            for j in range(i+1):
                st = s[j:c+1]
                if st == st[::-1]:
                    return st
                c += 1
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalin(S)

        print(ans)
# } Driver Code Ends