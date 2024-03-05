#User function Template for python3

class Solution:
    #Complete this function
    # Function to find the maximum index difference.
    def maxIndexDiff(self,s, n): 
        ##Your code here
        m = 0
        for i in range(len(s)//2):
            j = len(s)-1
            while s[i]>s[j]:
                j = j-1 
            m = max(m,j-i)
        return m    


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
            print(ob.maxIndexDiff(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends