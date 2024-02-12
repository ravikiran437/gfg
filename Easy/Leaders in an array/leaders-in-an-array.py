class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, l, N):
        #Code here
        arr = []
        k = []
        for i in l[::-1]:
            if k == []:
                k.append(i)
                arr.append(i)
            else:
                if k[-1] <= i :
                    k.pop()
                    k.append(i)
                    arr.append(i)
        return arr[::-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends