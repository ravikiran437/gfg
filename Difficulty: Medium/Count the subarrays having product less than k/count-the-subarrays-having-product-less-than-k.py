#User function Template for python3

class Solution:
    def countSubArrayProductLessThanK(self, l, n, k):
        #Code here
        c = 1 
        s = []
        a = 0
        cnt = 0
        for i in range(n):
            c *= l[i] 
            s.append(l[i])
            if c >= k :
                b = len(s)-1
                cnt += ((b*(b+1))//2)-(a*(a+1))//2
                while c >= k and s:
                    c = c//s.pop(0)
                a = len(s)-1
        b = len(s)
        cnt += ((b*(b+1))//2)-(a*(a+1))//2
        return cnt
    
    
    
    


#{ 
 # Driver Code Starts

#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        
        print(Solution().countSubArrayProductLessThanK(arr, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends