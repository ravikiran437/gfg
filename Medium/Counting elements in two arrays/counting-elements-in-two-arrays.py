#User function Template for python3
import bisect
class Solution:
    def countEleLessThanOrEqual(self,l1,n1,l2,n2):
        #returns the required output
        k = []
        l2.sort()
        for i in l1:
            index = bisect.bisect_right(l2,i)
            k.append(index)
        return k
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        
        n1,n2=[int(x) for x in input().split()]
        arr1=[int(x) for x in input().split()]
        arr2=[int(x) for x in input().split()]
    
        res = Solution().countEleLessThanOrEqual(arr1,n1,arr2,n2)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends