
class Solution:
    def countDistinct(self, l, N, k):
        # Code here
        d = {}
        for i in l[:k]:
            if i not in d:
                d[i] = 1 
            else:
                d[i] += 1 
        x = [len(d)]
        for i in range(k,len(l)):
            d[l[i-k]] -= 1 
            if d[l[i-k]] == 0:
                del d[l[i-k]]
            if l[i] not in d:
                d[l[i]] = 1 
            else:
                d[l[i]] += 1
            x.append(len(d))
        return x

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        res = Solution().countDistinct(arr, n, k)
        for i in res:
            print (i, end = " ")
        print ()
# } Driver Code Ends