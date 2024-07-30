#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, l):
        #Code here
        d = {0:-1}
        c = 0
        m = 0 
        for i in range(len(l)):
            c += l[i]
            if c not in d:
                d[c] = i 
            else:
                m = max(i-d[c],m)
        return m

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends