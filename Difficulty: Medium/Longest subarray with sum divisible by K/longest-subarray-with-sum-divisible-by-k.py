#User function Template for python3
class Solution:
	def longSubarrWthSumDivByK (self,arr,  n, k) : 
		#Complete the function
		pre = 0 
		d = {}
		m = 0 
		for i in range(n):
		    pre += arr[i]
		    if pre%k == 0 :
		        m = max(m,i+1)
		    else:
		        rem = pre % k 
		        if rem in d:
		            m = max(m,i-d[rem])
		        else:
		            d[rem] = i 
		return m
		    




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	for _ in range(0,int(input())):
		n, K = map(int ,input().split())
		arr = list(map(int,input().strip().split()))
		ob = Solution()
		res = ob.longSubarrWthSumDivByK(arr, n, K)
		print(res)




# } Driver Code Ends