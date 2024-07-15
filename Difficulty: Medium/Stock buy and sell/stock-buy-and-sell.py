#User function template for Python

class Solution:
    #Function to find the days of buying and selling stock for max profit.
	def stockBuySell(self, A, n):
		#code here
		m = A[0] 
		mini = 0 
		ind = 1 
		a = 0 
		l = []
		for i in A[1:]:
		    if mini == 0 and i < m:
		        m = i 
		        a = ind 
		    else:
		        if mini > i :
		            l.append([a,ind-1])
		            mini = 0 
		            m = i 
		            a = ind 
		        else:
		            mini = i 
		    ind = ind + 1
		if mini!=0:
		    l.append([a,ind-1])
# 		print(l)
		return l
	
		    


#{ 
 # Driver Code Starts
#Initial template for Python

def check(ans,A,p):
    c = 0
    for i in range(len(ans)):
        c += A[ans[i][1]]-A[ans[i][0]]
    if(c==p):
        return 1 
    else:
        return 0

if __name__=='__main__':
	t = int(input())
	while(t>0):
		n = int(input())
		A = [int(x) for x in input().strip().split()]
		ob = Solution()
		ans = ob.stockBuySell(A,n)
		p=0
		for i in range(n-1):
		    p += max(0,A[i+1]-A[i])
		if(len(ans) == 0):
			print("No Profit",end="")
		else:
			print(check(ans,A,p),end="")
		print()
		t-=1
# } Driver Code Ends