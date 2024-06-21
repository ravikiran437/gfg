#User function Template for python3


class Solution:
    def compareFrac (self, str):
        
        # code here
        l = str.split(",")
        d = 0
        a,b = "",""
        for i in l[0]:
            if i == "/":
                d = 1
            if i != " " and d == 0:
                a += i 
            elif i!=" "and d == 1 and i!= "/":
                b += i 
        c,d = "",""
        e = 0 
        for i in l[1]:
            if i == "/":
                e = 1
            if i != " " and e == 0:
                c += i 
            elif i!=" "and e == 1 and i!= "/":
                d += i 
        m = int(a)/int(b) 
        n = int(c)/int(d) 
        if m > n :
            return a+"/"+b
        elif m < n:
            return c+"/"+d
        return "equal"
        
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import re

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        str = input()
        print(ob.compareFrac(str))

# } Driver Code Ends