#User function Template for python3

class Solution:
    def rremove (self, s):
	def rec(s):
            if len(s) == 1:
                return s
            s += "@"
            l = list(s)
            p = []
            c = -1
            for i in range(len(l)-1):
                if l[i] == l[i+1]:
                    c = -3
                else:
                    if c==0 or c==-1:
                        p.append(l[i])
                    c = 0 
            m = "".join(p)
            if m == "":
                return ""
            m = m+"@"
            if m == s:
                return m[:-1]
            return rec(m[:-1])
        return rec(s)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range (t):
        S = input()
        ob = Solution()
        print(ob.rremove(S))


# } Driver Code Ends
