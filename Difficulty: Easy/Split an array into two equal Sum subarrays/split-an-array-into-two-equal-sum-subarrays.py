class Solution:
    def canSplit(self, arr):
        #code here
        s = sum(arr)
        k = 0 
        for i in arr:
            s -= i 
            k += i 
            if s == k:
                return 1 
        return 0

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])
    index = 1
    for _ in range(t):
        arr = list(map(int, data[index].split()))
        index += 1

        obj = Solution()
        res = obj.canSplit(arr)
        if (res):
            print("true")
        else:
            print("false")

# } Driver Code Ends