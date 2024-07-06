#User function Template for python3
class Solution:
	def minJumps(self, arr, n):
	    #code here
	    if n == 1:
	        return 0
	    dp = [arr[0]]
	    m = arr[0] 
	    for i in range(1,n):
	        if m < i :
	            return -1 
	        if i <= dp[-1]:
	            m = max(m,arr[i]+i)
	        else:
	            dp.append(m)
	            m = max(m,arr[i]+i)
	       # print(dp)
	    return len(dp)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends