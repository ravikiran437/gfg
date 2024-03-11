#User function Template for python3
class Solution:
	def countPairs(self, mat1, mat2, n, x):
		# code here
		l1,l2 = [],[]
        for i in mat1:
            l1 += i 
        for j in mat2:
            l2 += j 
        d1 = {}
        for i in l2:
            if i not in d1:
                d1[i] = 1 
            else:
                d1[i] += 1 
        c  = 0 
        for i in l1:
            p = x - i 
            if p in d1:
                d1[p] -= 1 
                c += 1
                if d1[p] == 0:
                    del d1[p]
        return c

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n , x = input().split()
		n,x = int(n), int(x)
		mat1 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat1.append(a)

		mat2 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat2.append(a)

		ob = Solution()
		ans = ob.countPairs(mat1, mat2, n, x)
		print(ans)

# } Driver Code Ends