#User function Template for python3

class Solution:
    def checkCompressed(self, s, t):
        # code here 
        p = ""
        a = ""
        for i in t:
            if i.isdigit():
                p += i 
            else:
                if p!="":
                    a += "-"*int(p) 
                    a += i
                    p = ""
                else:
                    a += i 
        if p!="":
            a += "-"*int(p) 
        if len(s) != len(a):
            return 0
        for i in range(len(s)):
            if a[i] != "-" and s[i] != a[i]:
                return 0
        return 1
                    
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S = input()
        T = input()
        
        ob = Solution()
        print(ob.checkCompressed(S,T))
# } Driver Code Ends