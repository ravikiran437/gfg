#User function Template for python3

class Solution:
    
    #Function to find maximum number of consecutive steps 
    #to gain an increase in altitude with each step.
    def maxStep(self, arr):
        # arr.sort()
        #Your code here
        m = 0 
        prev = arr[0]
        count = 0 
        for i in arr[1:]:
            if prev < i:
                count += 1 
            else:
                count = 0 
            prev = i 
            
            m = max(m,count)
        return m
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.maxStep(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends