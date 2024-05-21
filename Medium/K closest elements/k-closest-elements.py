#User function Template for python3

class Solution:
    def printKClosest(self, arr, n, k, x):
        # code here
        d = {}
        for i in arr:
            dif = abs(i-x)
            if dif!=0:
                if dif not in d:
                    d[dif] = [i]
                else:
                    d[dif].append(i)
        l = list(d.keys())
        l.sort()
        a,c = [],0
        dd = 1
        for i in l:
            if dd == 0 :
                break
            p = d[i]
            p.sort(reverse = True)
            for j in p:
                if c==k:
                    dd = 0
                    break
                else:
                    a.append(j)
                c += 1
        return a
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k, x = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.printKClosest(arr, n, k, x)
        for xx in ans:
            print(xx, end=" ")
        print()
        tc -= 1

# } Driver Code Ends