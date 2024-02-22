#User function Template for python3
class Solution:

	
	def search(self,p,t):
	    
	    # code here
	   # 
	    f=0
        for i in p:f+=hash(i)
        cnt = 0
        j = 0
        c = 0
        for i in range(len(t)):
            cnt += hash(t[i])
            if i>=len(p):
                cnt -= hash(t[j])
                j += 1 
            if f == cnt :
                c += 1 
        return c
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        txt=input().strip()
        pat=input().strip()
        ob = Solution()
        ans = ob.search(pat, txt)
        print(ans)
        tc=tc-1
# } Driver Code Ends