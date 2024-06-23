#User function Template for python3
class Solution:
	def bracketNumbers(self, str):
		# code here
        stack = []
        c = 1
        res = []
        for i in str:
            if i == "(":
                stack.append(c)
                res.append(c)
                c += 1 
            elif  i == ")":
                if stack:
                    res.append(stack[-1])
                    stack.pop()
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.bracketNumbers(S)
        for value in answer:
            print(value, end=" ")
        print()

# } Driver Code Ends