#User function Template for python3

class Solution:
    def maxSum(self,arr):
        # code here
        arr.sort()
        
        n = len(arr)
        
        temp = []
        
        for i in range(n//2):
            temp.append(arr[i])
            temp.append(arr[n-i-1]) 
        
        if n&1 == 1:
            temp.append(arr[n//2])
        
        total  =  0 
        
        for i in range(len(temp)-1):
            total += abs(temp[i]-temp[i+1])
            
        total += abs(temp[0] - temp[-1])
        
        return total

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.maxSum(arr)  # Call maxSum method and store result in ans
        print(ans)  # Print the result
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends