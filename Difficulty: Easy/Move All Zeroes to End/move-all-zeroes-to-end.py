#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
    	c=0
        for i in range(len(arr)):
            if arr[i]!=0:
                arr[c]=arr[i]
                c+=1
        for i in range(c,len(arr)):
            arr[i]=0 
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends