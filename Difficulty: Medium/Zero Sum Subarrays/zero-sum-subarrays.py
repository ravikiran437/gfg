#User function Template for python3

class Solution:
    #Function to count subarrays with sum equal to 0.
    def findSubArrays(self,arr,n):
        d  ={0:1}
        #return: count of sub-arrays having their sum equal to 0
        count = 0 
        pre = 0 
        for i in arr:
            pre += i 
            if pre in d:
                count += d[pre]
                d[pre] += 1 
            else:
                d[pre] = 1 
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
        
if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        A = [int(x) for x in input().strip().split(' ')]
        ob = Solution()
        print(ob.findSubArrays(A,N))
        
                
                
# } Driver Code Ends