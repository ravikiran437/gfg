from typing import List


class Solution:
    def maximumProfit(self, nums) -> int:
        # code here
        a = nums[0]
        cnt = 0 
        maxi = 0 
        for i in nums[1:]:
            if maxi == 0 and a > i :
                a = i 
            else:
                if maxi > i :
                    cnt += maxi - a 
                    a = i 
                    maxi = 0 
                else:
                    maxi = i 
        if maxi !=0 :
            cnt += maxi-a
        return cnt


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.maximumProfit(arr)
        print(res)

# } Driver Code Ends