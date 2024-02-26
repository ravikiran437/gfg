#User function Template for python3

class Solution:
	def AllPossibleStrings(self, s):
		# Code here
		a = []
		for  i in range(1,2**len(s)):
		    x = ""
		    for j in range(len(s)):
		        if (i>>j)&1:
		            x += s[j]
		    a.append(x)
		a.sort()
		return a
		  
		        

#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends