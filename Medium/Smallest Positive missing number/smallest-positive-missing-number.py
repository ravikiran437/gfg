#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,nums,n):
        #Your code herepos
        nums.sort()
        c = 0 
        for i in range(len(nums)):
            if nums[i] > 0 and nums[i] == 1 and c == 0:
                c = 1 
                pre = 1
            elif c == 1 and pre == nums[i]:
                pass 
            elif c == 1 and nums[i]!=pre+1:
                return pre+1
            else:
                pre = nums[i]
        if c == 0:
            return 1 
        if pre == nums[-1]:
            return pre+1
#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math


def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            print(ob.missingNumber(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends