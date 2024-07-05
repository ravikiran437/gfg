#User function Template for python3

class Solution:

    def longestKSubstr(self, s, k):
        # code here
        d ={}
        m = 0 
        pp = -1
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = i
            else:
                d[s[i]] = i 
            if len(d) > k :
                pp = max(pp,i-m)
                p = ""
                mini = min(d.values())
                for i,j in d.items():
                    if j == mini :
                        p = i
                        break
                m = d[p]+1
                del d[p]
        if pp == -1 :
            if len(d) != k :
                return -1
            return len(s)
        pp = max(pp,len(s)-m)
        return pp
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends