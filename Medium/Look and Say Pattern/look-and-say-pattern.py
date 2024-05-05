#User function Template for python3

class Solution:

    def lookandsay(self, n):
        def fun(s):
            k = ""
            c = 1
            pre = s[0]
            for i in s[1:]:
                if pre == i :
                    c += 1 
                else:
                    k += str(c)+pre
                    c = 1 
                    pre = i
            k += str(c)+pre
            return k
        k  = ["1"]
        for i in range(n-1):
            k.append(fun(k[-1]))
        return int(k[-1])
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())

        solObj = Solution()

        print(solObj.lookandsay(n))

# } Driver Code Ends