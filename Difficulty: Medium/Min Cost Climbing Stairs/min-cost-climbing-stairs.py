#Back-end complete function Template for Python 3

class Solution:
    def minCostClimbingStairs(self, cost):
        #Write your code here
        if len(cost) <= 2:
            return min(cost)
        for i in range(2,len(cost)):
            cost[i] = cost[i] + min(cost[i-1],cost[i-2])
        return min(cost[-1],cost[-2])
        
            


#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))  # Input array
    obj = Solution()
    res = obj.minCostClimbingStairs(arr)
    print(res)
    print("~")

# } Driver Code Ends