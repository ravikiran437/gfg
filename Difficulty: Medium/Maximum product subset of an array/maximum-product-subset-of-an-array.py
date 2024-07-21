#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def findMaxProduct(self, arr):
        # Write your code here
        if len(arr) == 1 :
            return  arr[0]
        l = []
        cnt = 0
        for i in arr:
            if i < 0:
                l.append(i)
            if i == 0:
                cnt += 1
        # print(l)
        l.sort()
        # print(l)
        if len(l) == 1 and cnt == len(arr)-1:
            return 0
        if l:
            k = l[-1]
        c = 0
        m = 1 
        d = 0
        mod = (10**9)+7
        for i in arr:
            if len(l)%2==1 and c == 0:
                if i == k and c == 0:
                    c = 1 
                elif i!=0:
                    m = (m*i)%mod
                    d = 1
            elif i!=0:
                d = 1
                m  = (m * i)%mod
        if d == 1:
            return m%mod
        return 0
    


#{ 
 # Driver Code Starts.
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        solution = Solution()
        ans = solution.findMaxProduct(arr)
        results.append(ans)
    
    for result in results:
        print(result)
# } Driver Code Ends