class Solution:
	def mergeOverlap(self, arr):
		#Code here
		a,b = [],[]
        for  i,j in arr:
            a.append(i)
            b.append(j)
        a.sort()
        b.sort()
        c = a[0]
        d = b[0]
        res = []
        for i in range(1,len(a)):
            if d >= a[i]:
                d = b[i]
            elif d < a[i]:
                res.append([c,d])
                c = a[i]
                d = b[i]
        res.append([c,d])
        return res


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        # a = list(map(int, input().strip().split()))
        arr = []
        # j = 0
        for i in range(n):
            a = list(map(int, input().strip().split()))
            x = a[0]
            # j += 1
            y = a[1]
            # j += 1
            arr.append([x, y])
        obj = Solution()
        ans = obj.mergeOverlap(arr)
        for i in ans:
            for j in i:
                print(j, end=" ")
        print()

# } Driver Code Ends