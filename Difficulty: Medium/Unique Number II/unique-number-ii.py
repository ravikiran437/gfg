#User function Template for python3
from collections import Counter
class Solution:
	def singleNum(self, nums):
		# Code here
		k=Counter(nums)
        n=[]
        for i,j in k.items():
            if j==1:
                n.append(i)
        n.sort()
        return n



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        ans = ob.singleNum(arr)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends