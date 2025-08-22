class Solution:
    def median(self, m):
    	# code here 
    	k=[]
        for i in m :
            k+=i 
        k.sort()
        return k[len(k)//2]