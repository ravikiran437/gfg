#User function Template for python3

class Solution:
    def longestCommonSubstr(self, str1, str2):
        # code here
        s = ""
        m = 0 
        for i in str1:
            if i in str2:
                s += i 
                if s in str2:
                    m = max(m,len(s))
                else:
                    s = i 
            else:
                s = ""
        return m


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S1 = input().strip()
        S2 = input().strip()
        ob = Solution()
        print(ob.longestCommonSubstr(S1, S2))

# } Driver Code Ends