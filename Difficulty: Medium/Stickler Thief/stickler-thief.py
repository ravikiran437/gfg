class Solution:  
    def findMaxSum(self,arr):
        # code here
        if len(arr) > 2:
            arr[2] += arr[0]
        for i in range(3,len(arr)):
            arr[i] = arr[i] + max(arr[i-2],arr[i-3])
        return max(arr[-1],arr[-2])


#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):

        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.findMaxSum(a))
        print("~")

# } Driver Code Ends