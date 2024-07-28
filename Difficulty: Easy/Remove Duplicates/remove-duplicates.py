#User function Template for python3
class Solution:
	def removeDups(self, str):
		# code here
		s  = set()
		k = ""
		for i in str:
		    if i not in s:
		        s.add(i)
		        k += i 
		return k


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.removeDups(s)

        print(answer)

# } Driver Code Ends