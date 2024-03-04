#User function Template for python3
class Solution:
    
    def countBuildings(self,h, n):
        # code here
        if n == 1:
            return 1
        c = h[0]
        cnt = 1
        for  i in h[1:]:
            if i>c:
                c = i 
                cnt += 1 
        return cnt
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        h = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countBuildings(h, n)
        print(ans)
        tc -= 1

# } Driver Code Ends