#User function Template for python3

class Solution:
    def CamelCase(self,N,dic,p):
        #code here
        k = []
        c = -1
        for i in dic:
            s = ""
            for j in i:
                if j.isupper():
                    s += j 
                    if s == p:
                        k.append(i)
                        break
        if k :
            return k 
        return [-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        Dictionary=list(map(str,input().split()))
        Pattern=input()
        ob=Solution()
        ans=ob.CamelCase(N,Dictionary,Pattern)
        ans.sort()
        for i in ans:
            print(i,end=" ")
        print()    
# } Driver Code Ends