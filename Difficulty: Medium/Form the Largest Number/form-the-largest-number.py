class Solution:

	def findLargest(self, arr):
	    k = []
	    for i in arr:
	        k.append([str(i)*10,i])
	    
	    k.sort(reverse = True)
	    
	    result = ""
	    for i,j in k:
	        result += str(j)
	     
	    result = result.lstrip("0")
        
        return result if result else "0"
	    