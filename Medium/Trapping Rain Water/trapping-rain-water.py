
class Solution:
    def trappingWater(self, h,n):
        #Code here
        pre,suf = [],[]
        m,n = h[0],h[-1]
        pre.append(h[0])
        suf.append(h[-1])
        for i in range(1,len(h)):
            if h[i] > m :
                m = h[i]
            pre.append(m)
        for j in range(len(h)-2,-1,-1):
            if h[j] > n:
                n = h[j]
            suf.append(n)
        suf = suf[::-1]
        ans = 0 
        for i in range(len(pre)):
            ans += min(abs(suf[i]-h[i]),(abs(pre[i]-h[i])))
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends