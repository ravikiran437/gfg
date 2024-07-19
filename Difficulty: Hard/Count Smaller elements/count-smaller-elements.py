#User function Template for python3
import bisect
class Solution:

	def constructLowerArray(self,l):
		# code here\
		arr = []
		p = []
        for i in l[::-1]:
            k = bisect.bisect_left(arr,i)
            arr.insert(k,i)
            p.append(k)
        return p[::-1]
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.constructLowerArray(arr)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends