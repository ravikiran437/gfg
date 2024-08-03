#User function Template for python3

class Solution:
    def asteroidCollision(self, N, a):
        # Code here
        stack = []
        for i in a:
            d = 0 
            while stack and stack[-1] > 0 and i < 0 :
                if stack[-1] < -i:
                    stack.pop()
                    continue 
                elif stack[-1] == -i:
                    stack.pop()
                break
            else:
                stack.append(i)
        return stack


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        asteroids = list(map(int, input().split()))
        ob = Solution()
        res = ob.asteroidCollision(N, asteroids)
        for val in res:
            print(val, end = ' ')
        print()
# } Driver Code Ends