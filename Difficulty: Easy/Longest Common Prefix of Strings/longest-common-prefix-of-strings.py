#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        if len(arr) == 1:
            return arr[0]
        arr.sort()
        a = arr[0]
        b = arr[-1]
        s = ""
        for i in range(len(a)):
            if a[i] == b[i]:
                s += a[i]
            else:
                break 
        if s == "":
            return -1 
        return s
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        arr = [x for x in input().strip().split(" ")]

        ob = Solution()
        print(ob.longestCommonPrefix(arr))

# } Driver Code Ends