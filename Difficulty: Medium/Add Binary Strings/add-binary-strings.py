#User function Template for python3
class Solution:
	def addBinary(self, A, B):
		# code here
		a=bin(int(A,2)+int(B,2))
        return a[2:]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        a = input().strip()
        b = input().strip()
        ob = Solution()
        answer = ob.addBinary(a, b)

        print(answer)
        print("~")

# } Driver Code Ends