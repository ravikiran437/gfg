#User function Template for python3

class Solution:
    def removeKdigits(self, s: str, k: int) -> str:
        if len(s) <= k:
            return "0"

        stack = []
        for digit in s:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        # If there are still digits to remove, remove from the end
        stack = stack[:-k] if k > 0 else stack

        # Convert the stack back to a string and strip leading zeros
        result = "".join(stack).lstrip('0')
        
        # If the result is an empty string, return "0"
        return result if result else "0"
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