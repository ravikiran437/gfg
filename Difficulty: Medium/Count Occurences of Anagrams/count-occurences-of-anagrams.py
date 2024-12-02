#User function Template for python3
class Solution:

	
	def search(self,pat, txt):
	    # code here
	    
	    l =[0]*26 
	    for i in pat:
	        l[ord(i)-97] += 1 
	    k = [0]*26 
	    count = 0 
	    for i in range(len(txt)):
	        k[ord(txt[i])-97] += 1
	        if i >= len(pat):
	            p = i-len(pat)
	            k[ord(txt[p])-97] -= 1 
	        if l == k:
	            count += 1 
	    return count
	        
	            
	        
	    
	    


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
        print("~")
# } Driver Code Ends