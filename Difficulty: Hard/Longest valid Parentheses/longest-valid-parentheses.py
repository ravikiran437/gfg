# User function Template for Python3

class Solution:
    def maxLength(self, s):
        # code here
        k = [0] * len(s)
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif stack != [] and s[i] == ")":
                k[stack[-1]] = 1 
                stack.pop()
                k[i] = 1 
        m = 0
        c=  0 
        for i in k:
            if i == 1:
                c += 1 
            else:
                m = max(c,m)
                c = 0 
        m = max(c,m)
        return m
                








#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.maxLength(S))
        print("~")

# } Driver Code Ends