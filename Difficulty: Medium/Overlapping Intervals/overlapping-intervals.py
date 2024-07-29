class Solution:
	def overlappedInterval(self, arr):
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
    T=int(input())
    for i in range(T):
    	n = int(input())
    	a = list(map(int, input().strip().split()))
    	Intervals = []
    	j = 0
    	for i in range(n):
    		x = a[j]
    		j += 1
    		y = a[j]
    		j += 1
    		Intervals.append([x,y])
    	obj = Solution()
    	ans = obj.overlappedInterval(Intervals)
    	for i in ans:
    		for j in i:
    			print(j, end = " ")
    	print()
# } Driver Code Ends