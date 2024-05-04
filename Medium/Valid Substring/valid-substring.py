#User function Template for python3

class Solution:
    def findMaxLen(ob, s):
        # code here 
        k = [-1]*len(s)
        st  = []
        for i in range(len(s)):
            if s[i] == "(":
                st.append(["(",i])
            elif st !=[] and s[i] == ")":
                k[st[-1][-1]] = 0 
                k[i] = 0 
                st.pop()
        c = 0 
        m = 0 
        for i in k:
            if i == 0 :
                c += 1 
            else:
                m = max(c,m)
                c = 0
        m = max(c,m)
        return m


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        
        ob = Solution()
        print(ob.findMaxLen(S))
# } Driver Code Ends