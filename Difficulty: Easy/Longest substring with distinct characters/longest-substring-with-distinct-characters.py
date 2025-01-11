#User function Template for python3

class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        t = ""
        m = 0 
        for i in s:
            if i not in t:
                t += i 
            else:
                m = max(m,len(t))
                t = t[t.find(i)+1:]
                t= t+i
        m = max(m,len(t))
        return m
                
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.longestUniqueSubstr(s)

        print(ans)

        print("~")
# } Driver Code Ends