#User function Template for python3


class Solution:
	def threeDivisors(self, query, q):
	    def prime(n):
	        if n < 2:
	            return 0 
	        for i in range(2,int(n**0.5)+1):
	            if n % i == 0:
	                return 0 
	        return 1 
	    k = []
	    for i in query :
	        c = 0 
	        for j in range(1,int(i**0.5)+1):
	            if prime(j) == 1:
	                c += 1 
	        k.append(c)
	    return k
	                
	    


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		q = int(input())
		query = []
		for _ in range(q):
			query.append(int(input()))
		
		ob = Solution()
		ans = ob.threeDivisors(query,q)
		for a in ans:
			print(a)

# } Driver Code Ends