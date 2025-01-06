#User function Template for python3
class Solution:
    def sumClosest(self, arr, t):
        # code here
        arr.sort()
        i = 0 
        j = len(arr)-1 
        m = float("inf")
        p = []
        while i < j :
            s = arr[i] + arr[j]
            if abs(t-s) < abs(t-m):
                m = s 
                p = [arr[i],arr[j]]
            
            if s > t:
                j -= 1 
            elif s < t:
                i += 1 
            else:
                break
        return p
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    while t > 0:
        arr = list(map(int, input().strip().split()))
        target = int(input().strip())
        ob = Solution()
        ans = ob.sumClosest(arr, target)
        if not ans:
            print("[]")
        else:
            print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends