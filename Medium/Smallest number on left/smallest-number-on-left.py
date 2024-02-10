# User function Template for Python3

class Solution:
    def leftSmaller(self, n, l):
        # code here
        k = []
        arr = []
        for i in l:
            if k == []:
                k.append(i)
                arr.append(-1)
            else:
                while len(k)!= 0 :
                    if k[-1]>=i:
                        k.pop()
                    else:
                        arr.append(k[-1])
                        k.append(i)
                        break
                else:
                    k.append(i)
                    arr.append(-1)
        return arr

#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input().split()
        for i in range(n):
            a[i] = int(a[i])
        
        ob = Solution()
        ans = ob.leftSmaller(n, a)
        for u in(ans):
            print(u,end = " ")
        print()
# } Driver Code Ends