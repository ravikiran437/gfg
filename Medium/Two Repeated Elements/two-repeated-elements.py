#User function Template for python3

class Solution:
    
    #Function to find two repeated elements.
    def twoRepeated(self, arr , n):
        #Your code here
        d = {}
        k = []
        for i in arr:
            if  i not in d:
                d[i] = 1 
            else:
                k.append(i)
        return k

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
            ans = obj.twoRepeated(A,N)
            print(ans[0], ans[1])
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends