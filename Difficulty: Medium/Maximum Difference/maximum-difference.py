class Solution:
    def findMaxDiff(self, arr):
        # code here
        stack = [arr[0]]
        k = [0]
        for i in arr[1:]:
            while stack and stack[-1] >= i:
                stack.pop()
            if stack == []:
                k.append(0)
            else:
                k.append(stack[-1])
            stack.append(i)
        stack1 = [arr[-1]]
        k1 = [0]
        for i in range(len(arr)-2,-1,-1):
            while stack1 and stack1[-1] >= arr[i]:
                stack1.pop()
            if stack1 == []:
                k1.append(0)
            else:
                k1.append(stack1[-1])
            stack1.append(arr[i])
 
        k = k[::-1]
        m = 0 
        for i in range(len(k)):
            m = max(m,abs(k[i]-k1[i]))
        return m

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.findMaxDiff(arr))

# } Driver Code Ends