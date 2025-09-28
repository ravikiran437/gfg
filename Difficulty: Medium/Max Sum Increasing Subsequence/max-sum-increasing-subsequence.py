#User function Template for python3
class Solution:
	def maxSumIS(self, arr):
	    
		# code here
		n = len(arr)
        dp = arr[:]  # each element as starting subsequence
        
        for i in range(n):
            for j in range(i):
                if arr[j] < arr[i]:
                    dp[i] = max(dp[i], dp[j] + arr[i])
        
        return max(dp)