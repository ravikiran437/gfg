#User function Template for python3

class Solution:

    def removeKdigits(self, num, k):
        stack = []
        for i in num:
            while k and stack and stack[-1]>i :
                stack.pop()
                k -= 1 
            stack.append(i)
        if k !=0:
            stack = stack[:-k]
        if stack == []:
            return "0"
        p = "".join(stack)
        p = p.lstrip("0")
        if p == "":
            return "0"
        return p 
            
        
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()
        K = int(input())

        obj = Solution()

        ans = obj.removeKdigits(S, K)

        print(ans)


# } Driver Code Ends