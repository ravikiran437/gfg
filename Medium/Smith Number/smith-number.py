#User function Template for python3

class Solution:
    def smithNum(self, n):
        if n == 2:
            return 0
        def add(num):
            c = 0
            while num:
                k = num % 10
                c += k 
                num = num // 10 
            return c
        tem = n
        s = add(n)
        c = 0 
        k =[]
        for i in range(2,int(n**0.5)+1):
            while n%i == 0:
                c += add(i)
                n = n //i 
        if n>1 and  n!=tem:
            c += add(n)
        if s == c:
            return 1
        return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        
        ob = Solution()
        print(ob.smithNum(n))
# } Driver Code Ends