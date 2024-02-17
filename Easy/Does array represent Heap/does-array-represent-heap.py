
class Solution:
    def isMaxHeap(self,l,n):
        d = {}
        c = 1
        for i in l:
            if c >= len(l):
                break
            d[i] = [l[c]]
            c += 1 
            if c >= len(l):
                break
            d[i].append(l[c])
            c += 1 
        c = 0
        for i,j in d.items():
            for k in j:
                if i<k:
                    c = 1
            if c == 1:
                return 0             
        return 1


#{ 
 # Driver Code Starts
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ob=Solution()
        print(int(ob.isMaxHeap(arr,n)))
# } Driver Code Ends