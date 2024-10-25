class Solution:
    def alternateSort(self,arr):
        # Your code goes here
        arr.sort()
        k = []
        n = len(arr)
        for i in range(n//2):
            k.append(arr[n-i-1])
            k.append(arr[i])
        if n % 2 == 1:
            k.append(arr[(n//2)])
        return k
#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.alternateSort(arr)
        print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends