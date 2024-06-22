#User function Template for python3
class Solution:
	
	def findMaxSum(self,arr, n):
		# code here
		if n <=2:
		    return max(arr)
		dp = [arr[0],arr[1]]
		for i in range(2,n):
		    if i>2:
		        a = max(dp[-2],dp[-3]) + arr[i]
		    else:
		        a = dp[-2]+arr[i]
		    dp.append(a)
		return max(dp)
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends