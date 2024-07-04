#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self, nums, s, n): 
        c = 0
        start = 0
        d = 0
        for end in range(s):
            c += nums[end]
            
            while c > n and start <= end:
                c -= nums[start]
                start += 1
                d += 1
            
            if c == n and d!=end+1:
                return [start + 1, end + 1]
                
        return [-1]
                    
        
        
            

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends