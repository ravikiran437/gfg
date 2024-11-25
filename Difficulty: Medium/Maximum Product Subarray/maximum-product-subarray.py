#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
		# code here
		suf = 1 
        pre = 1 
        m = float("-inf")
        n = len(arr)
        for i in range(n):
            pre = pre*arr[i]
            suf = suf*arr[n-i-1]
            m = max(pre,suf,m)
            if pre == 0 :
                pre = 1 
            if suf == 0:
                suf = 1 
        return m


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends