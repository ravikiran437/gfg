#User function Template for python3
class Solution:
    def kPangram(self,string, k):
        l = [0]*26 
        for i in string:
            if i!=" ":
                l[ord(i)-97] += 1
        p = l.count(0)
        c = 0 
        for i in l:
            if i >1:
                c += (i-1)
        if min(c,k) >= p :
            return 1
        return 0
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        string = input()
        K = int(input())
        ob = Solution()
        a = ob.kPangram(string, K)
        if a:
            print("true")
        else:
            print("false")

# } Driver Code Ends